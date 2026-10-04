# Dimension-two finite-field SICs outside characteristics two and three
## Finding
Let \(q\) be a prime power with \(\gcd(q,6)=1\). A unitary geometry on \(\mathbb F_{q^2}^{2}\), with Hermitian form \(\langle x,y\rangle=x^{*}y\), admits an equiangular tight frame of four vectors if and only if
\[
q\equiv2\pmod 3,
\]
equivalently \(3\mid(q+1)\).

More precisely, every such frame can be multiplied by one common nonzero scalar so that its parameters are \((a,b,c)=(1,1/3,2)\). After a unitary transformation, a permutation, and independent rescalings of the four vectors by elements of the norm-one torus
\[
\mathbb T_q=\{u\in\mathbb F_{q^2}^{\times}:u^{q+1}=1\},
\]
every normalized frame has representatives
\[
v_0=(1,0),\qquad
v_1=(\mu,\rho),\qquad
v_2=(\mu,\rho\omega),\qquad
v_3=(\mu,\rho\omega^2),
\]
where
\[
\mu^{q+1}=1/3,\qquad \rho^{q+1}=2/3,
\]
and \(\omega\in\mathbb T_q\) has order three.

## Assumptions and scope
The field is \(\mathbb F_{q^2}\) with conjugation \(z\mapsto z^q\), and \(q\) is any prime power whose characteristic is neither two nor three. The statement concerns the four-vector, two-dimensional unitary ETF problem. It does not classify the characteristic-two or characteristic-three cases.

An \((a,b,c)\)-ETF means four nonzero vectors that span \(\mathbb F_{q^2}^2\), have common Hermitian norm \(a\), have \(\langle v_i,v_j\rangle\langle v_j,v_i\rangle=b\) for \(i\ne j\), and satisfy \(\sum_i v_i v_i^*=cI\).

## Proof
Let \(\{x_i\}_{i=0}^3\) be a four-vector ETF in dimension two. The standard trace identity for an equal-norm tight frame gives \(4a=2c\), so \(c=2a\). The ETF parameter identity
\[
a(c-a)=3b
\]
therefore gives
\[
b=a^2/3.
\]
If \(a=0\), then \(b=0\). In that case every self-inner product and every pairwise inner product vanishes. Since the vectors span the two-dimensional space, the Hermitian form would vanish identically on the whole space, contradicting nondegeneracy. Thus \(a\ne0\).

The norm map \(N(z)=z^{q+1}\) from \(\mathbb F_{q^2}^{\times}\) onto \(\mathbb F_q^{\times}\) is surjective. Hence a common scalar rescaling makes \(a=1\), and then \(b=1/3\), \(c=2\).

Apply a unitary transformation sending \(x_0\) to \(e_1=(1,0)\). Write \(x_j=(\alpha_j,\beta_j)\) for \(j=1,2,3\). Since
\[
N(\langle e_1,x_j\rangle)=N(\alpha_j)=1/3
\]
and \(N(\alpha_j)+N(\beta_j)=1\), we have \(N(\beta_j)=2/3\). Choose \(\mu,\rho\in\mathbb F_{q^2}^{\times}\) with \(N(\mu)=1/3\) and \(N(\rho)=2/3\). Multiplying each \(x_j\), \(j=1,2,3\), by a suitable element of \(\mathbb T_q\) makes its first coordinate equal to \(\mu\). Thus
\[
x_j=(\mu,\rho u_j),\qquad u_j\in\mathbb T_q.
\]
For distinct \(i,j\in\{1,2,3\}\), put \(t=u_i^{-1}u_j\in\mathbb T_q\). Equiangularity gives
\[
N\!\left(\frac{1+2t}{3}\right)=\frac13.
\]
Since \(N(t)=1\), this is equivalent to
\[
(1+2t)(1+2t^{-1})=3,
\]
hence
\[
t+t^{-1}=-1,
\]
or
\[
t^2+t+1=0.
\]
Because the characteristic is not three, \(t\ne1\), so \(t\) has order three. Therefore \(\mathbb T_q\), which has order \(q+1\), contains an element of order three. Hence \(3\mid(q+1)\), equivalently \(q\equiv2\pmod3\).

The same argument also yields the normal form. After multiplying the second coordinate by a unimodular scalar, take \(u_1=1\). Then the pairwise ratio condition forces \(\{u_1,u_2,u_3\}=\{1,\omega,\omega^2\}\) for a primitive cube root \(\omega\in\mathbb T_q\).

Conversely, suppose \(3\mid(q+1)\). Choose \(\omega\in\mathbb T_q\) of order three and choose \(\mu,\rho\) with the prescribed norms. The four displayed vectors have norm one. Their inner products with \(v_0\) have norm product \(1/3\). For two distinct vectors among \(v_1,v_2,v_3\), their phase ratio is \(\omega\) or \(\omega^2\), so using \(1+\omega+\omega^2=0\) gives squared Hermitian magnitude \(1/3\). Finally,
\[
\sum_{j=0}^3 v_jv_j^*=2I
\]
because the diagonal entries are \(1+3(1/3)=2\) and \(3(2/3)=2\), while the off-diagonal sum contains the factor \(1+\omega+\omega^2=0\). Hence the vectors form a \((1,1/3,2)\)-ETF.

## Verification
The proof uses only the ETF trace identities, surjectivity of the quadratic finite-field norm, the cyclicity and order \(q+1\) of \(\mathbb T_q\), and direct Hermitian inner-product calculations. The necessity reduces to the exact polynomial identity \(t^2+t+1=0\) for a norm-one phase ratio; outside characteristic three this is equivalent to the existence of an element of order three in \(\mathbb T_q\).

The boundary assumptions are essential to this proof: characteristic two makes the coefficients involving \(2\) singular, while characteristic three permits the isotropic zero-norm phenomenon used by known \(\mathbb F_9\) examples.

## Relationship to prior work
Greaves, Iverson, Jasper, and Mixon developed finite-field unitary ETF theory and posed the general problem of determining the pairs \((d,q)\) for which a unitary geometry on \(\mathbb F_{q^2}^d\) admits an ETF of \(d^2\) vectors. Their paper also tabulates some finite fields admitting projected complex Gabor ETFs in dimension two, but it does not give an if-and-only-if classification for all prime powers \(q\). The result here determines the entire \(d=2\) slice away from characteristics two and three and explains the obstruction by the order-three subgroup of the norm-one torus.

Jorquera and King give newer structural criteria for finite-field ETFs, including a triple-product condition, but the inspected work does not state this two-dimensional unitary congruence classification. Iverson and Mixon's later finite-field SIC construction from modular Hadamard matrices specializes in dimension two to characteristic three under its stated congruence hypothesis, so it does not cover the characteristic-coprime-to-six classification proved here.

## Limitations
The characteristic-two and characteristic-three cases are deliberately excluded. In characteristic three, four-vector ETFs may be totally isotropic with zero frame constant, so the nonisotropic normalization used above is unavailable. No claim is made here about those modular cases or about dimensions larger than two.

The literature comparison found no statement implying the exact congruence classification, but a residual priority risk remains from specialized finite-geometry literature that may use different terminology for the same four-line unitary configuration.

## References
1. G. R. W. Greaves, J. W. Iverson, J. Jasper, D. G. Mixon, *Frames over finite fields: Basic theory and equiangular lines in unitary geometry*, arXiv:2012.12977; Finite Fields and Their Applications 77 (2022), 101954.
2. I. Jorquera, E. J. King, *On the Structure of Frames and Equiangular Lines over Finite Fields and their Connections to Design Theory*, arXiv:2505.12175.
3. J. W. Iverson, D. G. Mixon, *Asymmetric SICs over finite fields*, arXiv:2506.20778.
