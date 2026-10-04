# Same-model scientific review

## Correctness
PASS. The Daugavet lower bound uses only that every slice contains points of norm arbitrarily close to \(1\), while coordinate slices give the matching upper limit \(1-|t|\). For the Delta lower bound, every slice containing \((t,0)\) also contains the exact transverse unit-ball boundary point \((t,(1-t^p)^{1/p}u)\) after choosing the sign of \(u\) so the transverse functional contribution is nonnegative. The matching upper bound reduces to the scalar function \(F_t(s)=|s-t|^p+1-|s|^p\), whose behavior on the two intervals adjacent to \(t\) gives the sharp limit. The endpoint cases \(t=0\) and \(t=1\) are handled separately.

## Originality
PASS. The qualitative absolute-sum literature treats Delta points on the unit sphere. The quantitative source defines the constants and proves general stability inequalities, an exact \(\ell_1\)-sum zero-component statement on the unit sphere, and the Hilbert-space formula. The inspected statements do not give the universal scalar-axis formula for \(\mathbb R\oplus_pY\) with arbitrary nonzero \(Y\), nor the strict interior separation between the two constants.

## Value
PASS. Scalar axes are the canonical one-dimensional probes of an absolute sum. The formula isolates a universal transverse effect: the Daugavet constant stays at the one-dimensional value \(1-|t|\), whereas the Delta constant jumps to \((1-|t|^p)^{1/p}\) as soon as any nonzero transverse summand is present. This gives an exact quantitative stability law independent of the geometry of the added Banach space and extends the Hilbert-axis expression to arbitrary transverse spaces.

## Closest literature and limitations
The closest sources are arXiv:2001.06197 and arXiv:2307.10647. The result is restricted to real scalar-axis points and \(1<p<\infty\). The packaged rational replay checks only finite algebraic instances for integer exponents and is not an independent audit or a substitute for the analytic proof. An equivalent result under different terminology or in unindexed literature remains a residual bibliographic risk.

Same-model review: passed. Independent audit: not yet performed.
