from verify_square_bouquet import local_classes,order_faces,predicted_faces

def free_pair(faces,allowed):
    # A top simplex and one of its codimension-one free faces, both removable.
    for top in sorted(allowed,key=lambda s:(-s.bit_count(),s)):
        if any(top!=b and top & b == top for b in faces):continue
        bits=top
        while bits:
            low=bits & -bits;bits-=low
            sub=top ^ low
            if sub not in allowed or sub not in faces:continue
            if not any(b!=top and b!=sub and sub & b == sub for b in faces):
                return sub,top
    return None

_,classes=local_classes()
for p in (2,3):
    arcs,face0=order_faces(p)
    base,all_=predicted_faces(p,arcs,classes)
    assert face0==all_
    active=all_-{0};target=base-{0};pairs=[]
    while active!=target:
        removable=active-target
        pair=free_pair(active,removable)
        if pair is None:
            print('STUCK',p,len(removable));break
        active.difference_update(pair);pairs.append(pair)
    assert active==target
    print('p=',p,'relative_collapses=',len(pairs),'target_faces=',len(target),'PASS')
