# Trace-quadratic rigidity and exact phase census for binary Gold-graph Fourier extremizers

## Finding

For integers \(m>k\ge1\), put \(d=\gcd(m,k)\), \(r=m/d\), and assume \(d\ge2\) and \(r\ge2\). Let \(F=\mathbb F_{2^m}\), \(K=\mathbb F_{2^d}\), and choose any \(K\)-basis \(e_1,\dots,e_r\) of \(F\). Write every \(t\in F\) uniquely as \(t=\sum_i e_i y_i\), with \(y_i\in K\).

Let \(\psi:F\to\{\pm1\}\) be a nontrivial additive character. For \(f:F\to\mathbb C\), define the Fourier extension operator
\[
Tf(u,v)=\sum_{t\in F} f(t)\psi\big(ut+v t^{2^k+1}\big),\qquad (u,v)\in F^2,
\]
with counting-measure \(\ell^2(F)\) and probability-measure \(L^4(F^2)\).

**The complete projective-extremizer census in the intermediate subfield regime** is
\[
\boxed{N_{m,k}=2^{\,d\binom{r+1}{2}}.}
\]
Every nonzero sharp \(\ell^2\to L^4\) extremizer is, up to a nonzero complex scalar, uniquely represented by
\[
\boxed{ f\left(\sum_{i=1}^r e_i y_i\right)=
(-1)^{\operatorname{Tr}_{K/\mathbb F_2}\left(\sum_{i=1}^r a_i y_i+\sum_{1\le i<j\le r}b_{ij}y_i y_j\right)},
\quad a_i,b_{ij}\in K. }
\]
These \(d\binom{r+1}{2}\) field-bit parameters are independent and enumerate distinct complex projective lines, not just a lower-bound subfamily. In particular, the discrete projective phase group is naturally an \(\mathbb F_2\)-vector space of dimension \(d\binom{r+1}{2}\).

The decisive auxiliary theorem is a complete line-affine rigidity statement: for any \(d\ge2\) and \(r\ge1\), a Boolean map \(g:K^r\to\mathbb F_2\) whose restriction to **every** affine \(K\)-line is affine as a map of the underlying \(\mathbb F_2\)-vector space \(K\) has the unique form
\[
g(y)=\epsilon+\operatorname{Tr}_{K/\mathbb F_2}\left(\sum_i a_i y_i+\sum_{i<j}b_{ij}y_i y_j\right),
\quad\epsilon\in\mathbb F_2,\quad a_i,b_{ij}\in K.
\]
Thus this natural line-restriction code has exact binary dimension \(1+d\binom{r+1}{2}\). The exact count above follows by quotienting out the global sign \((-1)^\epsilon\).

## Assumptions and scope

The fields have characteristic two and \(m>k\ge1\); the extremizer count concerns only \(d=\gcd(m,k)\ge2\) and \(r=m/d\ge2\). No primality assumption on \(m\) or \(d\) is imposed. The choice of \(K\)-basis changes coordinates but not the phase-code dimension or count. Scalars used to identify projective extremizers are **arbitrary nonzero complex numbers**. The Fourier norm convention above is essential; the sharp fourth-power norm in this setting is \(2^d+1-2^{d-m}\), included here solely to derive equality conditions rather than as the census contribution. Line-affine means \(\mathbb F_2\)-affine on the \(d\)-dimensional binary vector space underlying each \(K\)-line; it does not mean \(K\)-affine with a \(K\)-valued target.

## Proof

**1. Fourier equality conditions independently reconstructed.** Let \(q=2^m\), \(h=2^d\), and \(M=\sum_{t\in F}|f(t)|^2\). Character orthogonality gives
\[
\|Tf\|_4^4=\sum_{(s,z)\in F^2}\left|\sum_{t:\ t^{2^k+1}+(t+s)^{2^k+1}=z}f(t)f(t+s)\right|^2.
\]
For \(s\ne0\), the map \(t\mapsto s^{2^k}t+s t^{2^k}\) has kernel \(sK\): indeed, after setting \(t=su\), its equation is \(u^{2^k}=u\), whose fixed field is \(K\). Therefore every nonempty nonzero-\(s\) fiber is a coset of \(sK\) with exactly \(h\) points. Cauchy--Schwarz in each fiber gives
\[
\|Tf\|_4^4\le \bigg|\sum_t f(t)^2\bigg|^2+h\sum_{s\ne0,t}|f(t)f(t+s)|^2
\le (h+1)M^2-h\sum_t|f(t)|^4
\le\big(h+1-h/q\big)M^2.
\]
The last inequality is sharp by constant input. For a nonzero extremizer, equality in the final inequality makes all \(|f(t)|\) constant and positive. Equality in the first term requires all \(f(t)^2\) to have one argument, so \(f(t)=c(-1)^{g(t)}\) for a nonzero \(c\in\mathbb C\) and \(g:F\to\mathbb F_2\). Finally Cauchy equality is equivalent to \(g(t)+g(t+s)\) being constant as \(t\) ranges over each coset of \(sK\), for every \(s\ne0\). Because every nonzero direction on a \(K\)-line occurs as a scalar multiple of \(s\), this is equivalent to the restriction of \(g\) to each affine \(K\)-line being \(\mathbb F_2\)-affine. Conversely, a constant-modulus sign function satisfying this line condition realizes all equalities. This establishes the necessary-and-sufficient equality reduction without relying on an earlier classification.

**2. Every pairwise interaction is balanced.** Choose \(K\)-coordinates and work with \(g:K^r\to\mathbb F_2\). For any base \(y\), define \(D_{i,a}g(y)=g(y+a e_i)+g(y)\), where now \(e_i\) denotes a coordinate vector. Individual coordinate-line affinity implies that \(a\mapsto D_{i,a}g(y)\) is \(\mathbb F_2\)-linear. The mixed difference
\[
B_{ij,y}(a,b)=D_{i,a}D_{j,b}g(y)
\]
is hence \(\mathbb F_2\)-bilinear. Apply the line condition in direction \(ae_i+be_j\): comparing the binary additivity of its restriction at parameters \(\lambda,\mu\in K\), after cancelling the single-coordinate terms, yields
\[
B_{ij,y}(\lambda a,\mu b)=B_{ij,y}(\mu a,\lambda b).
\]
With \(\lambda=1\) this says \(B_{ij,y}(a,\alpha b)=B_{ij,y}(\alpha a,b)\) for every \(\alpha\in K\). Therefore \(B_{ij,y}(a,b)=L_{ij,y}(ab)\) for an \(\mathbb F_2\)-linear functional \(L_{ij,y}:K\to\mathbb F_2\), namely \(L_{ij,y}(z)=B_{ij,y}(z,1)\). The nondegenerate finite-field trace pairing gives a unique \(c_{ij}(y)\in K\) such that
\[
B_{ij,y}(a,b)=\operatorname{Tr}_{K/\mathbb F_2}\big(c_{ij}(y)ab\big).
\]

**3. No three-coordinate interactions occur.** For distinct \(i,j,\ell\), the triple mixed difference \(C_{ij\ell,y}(a,b,c)=D_{i,a}D_{j,b}D_{\ell,c}g(y)\) is \(\mathbb F_2\)-trilinear. Taking a third difference preserves each pairwise balancing identity from step 2. Balancing in all three pairs implies
\[
C_{ij\ell,y}(a,b,c)=\operatorname{Tr}_{K/\mathbb F_2}(\gamma(y)abc)
\]
for some \(\gamma(y)\in K\). Expand \(g(y+\lambda ae_i+\lambda be_j+\lambda ce_\ell)\) by commuting finite differences. Its single-coordinate terms are additive in \(\lambda\), its pairwise terms are trace functions of \(\lambda^2\) and thus also additive, while the triple term is \(\operatorname{Tr}(\gamma(y)abc\lambda^3)\). Hence the latter term must be additive for every \(a,b,c\in K\).

If \(\gamma(y)\ne0\), select distinct nonzero \(\lambda,\mu\in K\) (possible because \(|K|\ge4\)). Their cubic additivity defect is \(\lambda\mu(\lambda+\mu)\ne0\). Varying \(abc\) over \(K\), nondegeneracy of the trace forces a nonzero defect for some \(a,b,c\), contradiction. Thus every triple mixed difference vanishes at every base point.

**4. Trace-quadratic decomposition and uniqueness.** The subset finite-difference expansion of \(g(y_1,\ldots,y_r)\) at the origin has no summands indexed by sets of at least three coordinates, by step 3. Its one-coordinate terms are linear functionals \(K\to\mathbb F_2\), uniquely of the form \(\operatorname{Tr}(a_i y_i)\). Its two-coordinate terms are the balanced bilinear maps of step 2, uniquely \(\operatorname{Tr}(b_{ij}y_i y_j)\). The empty-set term is \(\epsilon=g(0)\). These coefficients are unique: evaluating at zero, then at points supported in one coordinate, then in two coordinates recovers them by nondegenerate trace duality. Conversely, along an arbitrary affine line \(y+\lambda v\), each displayed pair term has dependence of the form \(\operatorname{Tr}(A+B\lambda+C\lambda^2)\), an \(\mathbb F_2\)-affine function of \(\lambda\). Thus every displayed trace polynomial satisfies the line condition.

There are two choices for \(\epsilon\), \(2^d\) choices for each of \(r+\binom r2=\binom{r+1}{2}\) trace coefficients, and no duplications. Hence the complete line-affine code has cardinality \(2^{1+d\binom{r+1}{2}}\). For Fourier extremizers, quotienting by global sign identifies exactly the two choices of \(\epsilon\); no two distinct normalized sign functions are scalar multiples except by this global sign. The asserted projective census and parametrization follow.

## Verification

The standalone Python checker `artifacts/verify.py` independently constructs all binary line-affinity equations as exact binary row vectors and performs Gaussian elimination over \(\mathbb F_2\). For several distinct proper intermediate subfields, the resulting dimensions agree with the trace-quadratic formula. It also checks the Gold pair-sum fibers, the sharp fourth-moment defect identity, explicit equality witnesses, and small direct Walsh evaluations. The finite computations are confirmations only: steps 1--4 establish the theorem for **all** stated field sizes. Execute `python3 artifacts/verify.py` with Python 3 and no third-party dependencies.

## Relationship to prior work

Mockenhaupt--Tao establish finite-field Fourier restriction and its even-moment machinery, but not this projective binary Gold extremizer count. Delgado--Janwa address the differential structure of binary Gold and related APN maps; differential multiplicities supply step 1 but not the phase census. Guo--Kopparty--Sudan supply a general theory of affine-invariant lifted codes, including a degree-set criterion that can be applied to the present line-restriction code; their general result is substantial antecedent machinery, not a statement about Gold-graph Fourier extremizers, and the trace-quadratic formula here is proved directly without invoking their general degree-set classification. González-Riquelme--Oliveira e Silva concern sharp extension in other finite-field geometries, not this binary intermediate-subfield projective census. In the edge regime \(d=1\), any Boolean phase pattern satisfies the line condition; the exceptional unrestrictive case is deliberately excluded from the theorem. The contribution isolated here is the **complete intermediate-subfield trace-quadratic rigidity and exact Fourier extremizer census**, rather than a general sharp-norm result.

## Limitations

No enumeration of affine-equivalence orbits of the distinct projective lines is claimed. The theorem only concerns full-support complex extremizers of the displayed fourth-moment operator in characteristic two with \(d\ge2\) and \(r\ge2\); it does not classify higher even moments or other graph exponents. Other historical formulations of the same line-affine code, particularly in lifted Reed--Muller literature, could contain an equivalent dimension calculation; the general lifted-code machinery is explicitly acknowledged and exhaustive priority is not certified. A finite checker does not prove infinitely many parameter cases.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first public 2002-04-18), https://arxiv.org/abs/math/0204234.
2. M. Delgado and H. Janwa, *On the Conjecture on APN Functions*, arXiv:1207.5528 (first public 2012-07-23), https://arxiv.org/abs/1207.5528.
3. A. Guo, S. Kopparty and M. Sudan, *New affine-invariant codes from lifting*, arXiv:1208.5413 (first public 2012-08-27), https://arxiv.org/abs/1208.5413.
4. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (first public 2024-05-26), https://arxiv.org/abs/2405.16647.
