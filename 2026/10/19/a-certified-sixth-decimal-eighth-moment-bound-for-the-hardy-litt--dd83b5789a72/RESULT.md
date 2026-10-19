# A certified sixth-decimal eighth-moment bound for the Hardy–Littlewood frequency triple

## Finding

Let \(P(z)=a+bz+cz^3\) with arbitrary complex coefficients, and let \(K_8^8\) be the best constant in \(\int_0^{2\pi}|P(e^{it})|^8\,dt/(2\pi)\le K_8^8(|a|^2+|b|^2+|c|^2)^4\). Then \(9.221770<K_8^8\le9.221771\). Moreover, every nonzero maximizer has all three coefficients nonzero and its phases obey \(3\arg b\equiv2\arg a+\arg c\pmod{2\pi}\). The upper bound is proved by an exact-integer degree-eight Bernstein subdivision certificate requiring 81 nodes and maximum depth 13; the lower bound follows by direct exact evaluation at positive integer magnitudes \((576602,605492,548552)\). No exact algebraic expression or uniqueness of maximizing moduli is claimed.

## Assumptions and scope

We use normalized Haar measure on the complex unit circle, complex coefficients \(a,b,c\), and the frequency support \(\{0,1,3\}\). The norm denominator is the fourth power of coefficient energy. The inequalities concern the **sharp but not explicitly algebraically determined** eighth-moment constant. The phase statement concerns all actual maximizers, and does not characterize the maximizing positive coefficient magnitudes.

## Proof

For \(a,b,c\ge0\), set \(M(a,b,c)=\sum_{j=0}^{12}|[z^j](a+bz+cz^3)^4|^2\). This homogeneous degree-eight polynomial equals the normalized eighth moment by Parseval. For complex coefficients of absolute values \(a,b,c\), the triangle inequality applied separately to each coefficient of the fourth power gives the moment at most \(M(a,b,c)\). If \(abc>0\), alignment of the two terms contributing to the coefficient of \(z^3\) requires \(3\arg b\equiv2\arg a+\arg c\pmod{2\pi}\), and that relation aligns every collision. Thus it is necessary and sufficient for attaining \(M\) at fixed positive magnitudes.

Let \(T=(a^2+b^2+c^2)^4\), and \(F=9221771T-1000000M\). As a homogeneous polynomial of degree eight, \(F\) is nonnegative on the first octant if and only if its restriction to the barycentric simplex \(a+b+c=1\) is nonnegative. Four-way midpoint subdivision of the simplex acts on barycentric coordinates by the four explicitly coded triples of linear forms in the attached `verify_eighth_moment.py`; each substitution is scaled by \(2^8\) to preserve integer coefficients. Any homogeneous polynomial with nonnegative monomial coefficients is nonnegative on its simplex. The exact script recursively subdivides only triangles with a negative coefficient and establishes that all 61 leaves have nonnegative coefficients, after 81 visited nodes, with maximum subdivision depth 13. The four child simplices partition their parent. Induction up the finite tree proves \(F\ge0\) for all nonnegative \(a,b,c\), hence the universal upper bound.

For \((a,b,c)=(576602,605492,548552)\), the exact coefficient calculation verifies \(10^6M(a,b,c)>9221770(a^2+b^2+c^2)^4\), giving the strict lower bound. An optimizer exists by compactness of the coefficient-energy unit sphere. A polynomial with only two nonzero coefficients has eighth-moment ratio at most \(70/16\): the fourth power of a binomial has coefficients whose squared sum is maximized for equal squared magnitudes, yielding \(\sum_{j=0}^4\binom4j^2/16=70/16\). Since \(70/16<9.221770\), every maximizer has all three coefficients nonzero and the phase condition follows.

## Verification

Run `python3 verify_eighth_moment.py` from this package. It requires only the Python standard library. It constructs the full moment polynomial from the fourth convolution power, builds the four exact integer substitution maps, and checks the whole adaptive subdivision tree and an integer lower witness. The recorded output is in `certificate_output.txt`. In particular, these are exact finite integer checks, not floating-point optimization or a numerical claim about an infinite search.

## Relationship to prior work

Ciccone and Gonçalves (first public 2022-08-19) study sharp circle Fourier extension under arithmetic restrictions based on \(B_3\)-type structure, providing natural context for resonance-sensitive Fourier moments. Known estimates for the triple \(\{0,1,3\}\) concern the sixth moment, while known eighth-moment estimates for the consecutive \(\{0,1,2\}\) and first fourth-order-resonant \(\{0,1,4\}\) triples do not give the eighth-moment coefficient on \(\{0,1,3\}\). Frequency translation, dilation, and character duality do not identify these distinct additive collision configurations at convolution order four.

## Limitations

The constant is certified within a rational interval of width \(10^{-6}\); its exact algebraic value, uniqueness of the maximizing modulus profile, and quantitative stability have **not** been proved. The certificate relies on the included full integer checker and not a manual display of every subdivision coefficient. The phase assertion does not assert uniqueness of magnitudes. The literature comparison is best-knowledge; repository records with inaccessible full text remain a residual originality risk.

## References

- V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441 (first posted 2022-08-19), https://arxiv.org/abs/2208.09441.
- Published mathematical result: *Sharp sixth moments for the resonant three-character spectrum* (comparison concerns a different exponent), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-sixth-moments-for-the-resonant-three-character-spectrum--d468c421bb0c.
- Published mathematical result: *Sharp L8/L2 norm for the consecutive three-frequency spectrum* (different frequency support), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-l-8-l-2-norm-for-the-consecutive-three-frequency-spectrum--69c7d8c4e990.
- Published mathematical result: *Sharp eighth-moment norm at the first fourth-order resonance* (different frequency support), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-eighth-moment-norm-at-the-first-fourth-order-resonance--5598303b6ef1.
