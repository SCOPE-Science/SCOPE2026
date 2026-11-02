"""Independent arithmetic verification of four-round Moore-graph extension cells."""

def triple_cells(d,shape):
    # The three selected vertices have shape: path, one_edge,
    # independent_concurrent, or independent_separate.
    n=d*d+1
    if shape=='path':
        return {'none':(d-1)*(d-2),'single':(d-1,d-2,d-1),'pairs':(0,0,0),'triple':0}
    if shape=='one_edge':
        return {'none':(d-1)*(d-2),'single':(d-2,d-2,d-2),'pairs':(0,1,1),'triple':0}
    if shape=='independent_concurrent':
        return {'none':d*(d-3),'single':(d-1,d-1,d-1),'pairs':(0,0,0),'triple':1}
    if shape=='independent_separate':
        return {'none':d*d-3*d+1,'single':(d-2,d-2,d-2),'pairs':(1,1,1),'triple':0}
    raise ValueError(shape)

for d in (3,4,7,57):
    n=d*d+1
    for shape in ('path','one_edge','independent_concurrent','independent_separate'):
        row=triple_cells(d,shape)
        assert row['none']+sum(row['single'])+sum(row['pairs'])+row['triple']==n-3,(d,shape,row)
        assert min(row['single'])>0
        if d>=4:assert row['none']>0
        if d==3 and shape=='independent_concurrent':assert row['none']==0
        if shape=='one_edge':assert row['pairs']==(0,1,1)
        print('CELL',d,shape,row)
    assert d*d-2*d>0 and (d-1)*(d-2)>0
print('SYMBOLIC_EXTENSION_ARITHMETIC_OK')
