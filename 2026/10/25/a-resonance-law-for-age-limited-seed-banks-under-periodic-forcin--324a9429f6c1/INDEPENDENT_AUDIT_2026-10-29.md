# Independent mathematical audit

## correctness

PASS

Let a=g, b=s(1-g), and M_L(r) have top row ar and subdiagonal b. Total seed mass S_t satisfies N_{t+1}=ar_t S_t and S_{t+1}=(b+ar_t)S_t - a*b^L*r_{t-L} S_{t-L}, with age-out correction exact. A nonzero monodromy Floquet multiplier μ obeys S_{t+m}=μS_t. For L=km the recurrence reduces to S_{t+1}=[b+ar_t(1-b^L μ^-k)]S_t, yielding the symmetric characteristic-polynomial identity after cancelling μ-b^m. For L=km-1, the reduction [1+ab^L r_{t+1} μ^-k]S_{t+1}=(b+ar_t)S_t gives the second symmetric product identity. Reconstruction from age-zero cohorts excludes spurious Floquet sequences except µ=b^m, and polynomial continuation covers degeneracies. Direct independent SymPy symbolic characteristic comparisons for m=4 and L=1..5 gave exact zero differences at L=1,3,4, nonzero signed a²b²µ(H-J)² at L=2 and -a²b^6µ³(H-J)² at L=5. At L=2 equal determinants and trace(alternating)-trace(clustered)=a²b²(H-J)²>0 imply strict Perron ranking. For g=1/5,s=9/10,H=4,J=1/6,L=5 independent exact rational multiplication verified all five components of Pc*v-v and w-Pa*w positive for v=(104,50,2,2,27), w=(40,2,22,1,11). Collatz–Wielandt gives rho(Pc)>1>rho(Pa). Source checker.py fully inspected but finite tests do not replace arbitrary m,k proof.

## originality

PASS

Best-of-knowledge exact all-season-permutation isospectrality at L=km or km-1 and sharp four-season age-five ordering reversal. Classical periodic population matrices and weed crop-rotation order effects are prior, but use different age/depth structuring and do not visibly state these full-spectrum congruences.

## value

PASS

The result isolates a surprising exact all-permutation full-spectrum invariant at two natural seed-age/period congruence families, plus a sharp age-five reversal between clustered and alternating environmental patterns with a certified growth/decline witness. This provides a structural classification/boundary in a well-motivated age-structured periodic model, beyond a generic fact that matrix multiplication is order-sensitive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
