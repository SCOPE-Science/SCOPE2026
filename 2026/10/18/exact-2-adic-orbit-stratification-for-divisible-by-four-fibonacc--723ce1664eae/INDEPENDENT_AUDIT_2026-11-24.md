# Independent mathematical audit

## correctness

PASS

The companion matrix has determinant −1; its fixed states are (a,a) with ca=0 modulo 2^k, equivalent to the stated Smith factors and F_0=2^min(k,h). The identity M²−I=cM gives U_1=(c/2^h)M of odd determinant. Squaring M^{2^j}=I+2^{h+j−1}U_j produces U_{j+1}=U_j+2^{h+j−2}U_j²; the multiplier of the second term is even for h>=2 and j>=1, so all U_j act invertibly modulo 2^k. Thus the fixed states of each power of two are exactly the kernel of scalar multiplication by 2^{h+j−1}, giving F_j=2^{2 min(k,h+j−1)}. Saturation ensures there are no non-dyadic lengths. Subtracting adjacent F_j and dividing by 2^j gives the advertised multiplicities, also at k=1, k=h and k=h+1; summing the resulting geometric progression gives the displayed totals. Negative c has the same proof with odd signed unit. Equal cycle type gives permutation conjugacy; trace invariance rules out linear conjugacy when traces differ, as for c=4 and 12 modulo 16. An independent complete enumeration for 42 combinations checked exact cycle counts, fixed-point counts and totals; a separate independent traversal checked the 144 source parameter pairs through k=8. The induction, not extrapolation, proves the unrestricted result.

## originality

PASS

Credit is for the exact whole-state least-period census uniform over the repeated-root layer h>=2, not merely for canonical sequence periods, Smith normal form, or the orbit-count identity. The strongest inspected matching state census assumes h=1 and has unequal Smith valuations after the first doubling where the target has equal valuations. The nearby full-text primary results on the sequence or companion order do not provide the all-state kernel ranks for this layer. Comparison is limited to the checked sources.

## value

PASS

This gives an exact orbit inventory in the natural remaining even-coefficient layer, with arbitrary initial states rather than a single distinguished orbit. It quantifies the change from coordinate-swap dynamics below the valuation threshold to a full hierarchy of periods above it, explains invariance under variation of the odd part of c, and determines finite permutation equivalence. General order information or the neighboring h=1 census would not recover these multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
