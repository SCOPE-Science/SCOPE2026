from fractions import Fraction as Q

def delta(r,c,d):
    return (10*Q(c))**2 - 20*Q(r)*Q(d)

rows=[]
for d in range(-3,3):
    a2=Q(d+3,15)
    F=(2,1,d)
    Qq=(-3,0,-3-d)
    df=delta(*F); dq=delta(*Qq)
    rows.append((d,a2,df,dq,df>=0 and dq>=0))
    print(f'd_F={d:2d} alpha2={a2} DeltaF={df} DeltaQ={dq} both_BG={df>=0 and dq>=0}')
positive=[r for r in rows if r[1]>0 and r[4]]
assert positive==[]
assert rows[0][1]==0 and rows[0][4]
assert delta(-3,0,-4)==-240
print('positive_alpha_both_BG=[]')
print('Edual_candidate_quotient_Delta=-240')
print('CORRECTED_CENSUS_OK')
