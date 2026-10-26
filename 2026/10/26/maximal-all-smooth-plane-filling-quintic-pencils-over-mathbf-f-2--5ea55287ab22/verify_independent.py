"""Direct 2187-form geometric-smoothness check and Walsh/XOR pencil count."""
import json
from verify_census import all_local_forms, geometric_smooth, inverse_columns, jet_rows


def main():
    rows=jet_rows()
    forms=list(all_local_forms(inverse_columns(rows)))
    assert len(set(forms))==2187
    smooth={f for f in forms if geometric_smooth(f)}  # No projective-orbit shortcut.
    assert len(smooth)==1512
    pairs=sum((f^g) in smooth for i,f in enumerate(sorted(smooth))
              for g in sorted(smooth)[i+1:])
    assert pairs==50400
    vector=[0]*16384
    for form in smooth:
        jet=sum(((form&r).bit_count()&1)<<j for j,r in enumerate(rows))
        assert jet&127==0
        vector[jet>>7]=1
    for bit in range(14):
        h=1<<bit
        for a in range(0,16384,2*h):
            for i in range(a,a+h):
                u,v=vector[i],vector[i+h]
                vector[i],vector[i+h]=u+v,u-v
    numerator=sum(v**3 for v in vector)
    assert numerator%16384==0
    ordered=numerator//16384
    assert ordered==100800
    assert ordered//6==pairs//3==16800
    print(json.dumps({'geometric_smoothness_tests':2187,
                      'smooth_forms':len(smooth),'smooth_unordered_pairs':pairs,
                      'walsh_ordered_triples':ordered,'all_smooth_pencils':ordered//6},
                     sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    main()
