# Exact ordinary-thinning threshold and punctured parent for every beta-binomial law

## Finding
Let \(a,b>0\) be real and \(n\ge1\) an integer. Draw \(W\sim\mathrm{Beta}(a,b)\), and conditionally draw
\[
X_n\mid W\sim\mathrm{Binomial}(n,W).
\]
Thus \(X_n\) has the beta-binomial law with mass function
\[
\Pr(X_n=k)=\binom nk\frac{(a)_k(b)_{n-k}}{(a+b)_n},\qquad 0\le k\le n,
\]
where \((c)_j=c(c+1)\cdots(c+j-1)\) for \(j\ge1\), and \((c)_0=1\).

For a nonnegative integer-valued random variable \(Z\), ordinary *deterministic* \(\tau\)-thinning \(\tau\circ Z\) retains each item independently with common probability \(\tau\in(0,1]\). Define
\[
\rho(X_n)=\inf\left\{\tau\in(0,1]:X_n\stackrel d=\tau\circ Z
\text{ for some nonnegative integer-valued }Z\right\}.
\]
**Theorem.** For every \(a,b>0\) and integer \(n\ge1\),
\[
\boxed{\rho(X_n)=r_n:=\frac{a+n-1}{a+b+n-1}.}
\tag{1}
\]
At the minimum there is a **unique** parent law \(Z_n\), with \(q_j=\Pr(Z_n=j)\) and
\[
q_n=\frac{(a)_n}{(a+b)_n}\,r_n^{-n}>0,
\qquad q_{n-1}=0,
\tag{2}
\]
\[
\boxed{q_j=
\frac{(1-r_n)(j+2)(j+1)q_{j+2}+
(2-r_n)(n-1-j)(j+1)q_{j+1}}
{(n-j)(a+j)}\quad(0\le j\le n-2).}
\tag{3}
\]
Every \(q_j\) with \(0\le j\le n\), \(j\ne n-1\), is strictly positive. Thus for \(n\ge2\), the support is **exactly**
\[
\{0,1,\ldots,n\}\setminus\{n-1\}.
\]
For \(n=1\), the parent is simply \(Z_1=1\) almost surely.

For fixed shape parameters \(a,b\), the minimum parameter and the top-atom inflation have the exact asymptotic laws
\[
n(1-r_n)\longrightarrow b,
\qquad
\frac{\Pr(Z_n=n)}{\Pr(X_n=n)}=r_n^{-n}\longrightarrow e^b.
\tag{4}
\]

## Assumptions and scope
All shape parameters are arbitrary positive real numbers, not restricted to integers or symmetric beta densities. Every sample size \(n\ge1\) is covered. The parent is an arbitrary nonnegative integer-valued count and is **not required** to be a beta-binomial distribution or a beta mixture. The thinning probability \(\tau\) is a constant, not a latent random probability: beta-binomial thinning operators and quasi-Pólya thinning kernels are different operations.

Uniqueness is distributional. Independent retention conditional on the parent count is exactly the standard binomial thinning operation, rather than a coupling or a deterministic count map.

## Proof
**1. Inversion is forced and finite.** For any parent \(Z\), conditional thinning with probability \(\tau>0\) has generating function
\[
P_{\tau\circ Z}(z)=P_Z(1-\tau+\tau z).
\]
Since \(\Pr(X_n=n)>0\) and \(\Pr(X_n>n)=0\), every such parent satisfies \(\Pr(Z>n)=0\): for each \(m>n\), conditional \(\tau\)-thinning of \(m\) items has positive probability of exceeding \(n\). Therefore its probability-generating polynomial, if it exists, is necessarily
\[
Q_\tau(z)=\mathbb E\left(1-\frac W\tau+\frac W\tau z\right)^n
=\sum_{j=0}^n q_j(\tau)z^j.
\tag{5}
\]
A representation exists if and only if every coefficient of this unique polynomial is nonnegative, since \(Q_\tau(1)=1\). In particular,
\[
q_{n-1}(\tau)=\frac{n}{\tau^n}
\left(\tau\,\mathbb EW^{n-1}-\mathbb EW^n\right).
\tag{6}
\]
The beta moments are
\[
\mathbb EW^k=\frac{(a)_k}{(a+b)_k},\quad k\ge0,
\]
so
\[
\frac{\mathbb EW^n}{\mathbb EW^{n-1}}
=\frac{a+n-1}{a+b+n-1}=r_n.
\tag{7}
\]
Thus \(q_{n-1}(\tau)<0\) whenever \(0<\tau<r_n\). This proves \(\rho(X_n)\ge r_n\).

**2. Positivity of the forced polynomial at the proposed threshold.** Write \(r=r_n\) and \(Q=Q_r\). The beta integral or the terminating Gauss series gives
\[
Q(z)={}_2F_1\left(-n,a;a+b;\frac{1-z}{r}\right).
\tag{8}
\]
For clarity, the only identity needed from the terminating hypergeometric polynomial \(H(t)={}_2F_1(-n,a;a+b;t)\) is the differential equation
\[
t(1-t)H''(t)+[a+b-(a-n+1)t]H'(t)+naH(t)=0.
\tag{9}
\]
It follows directly by substituting the finite polynomial series
\[
H(t)=\sum_{k=0}^n
\frac{(-n)_k(a)_k}{(a+b)_k\,k!}t^k
\]
and checking successive coefficients. Thus (9) is a finite algebraic identity, not an appeal to a limiting assertion.

Substitute \(t=(1-z)/r\) in (9) and use \(r(a+b+n-1)=a+n-1\). After multiplication by the common factor, this gives
\[
(1-z)(z+r-1)Q''(z)
+\bigl[-(n-1)(2-r)+(n-a-1)z\bigr]Q'(z)
+naQ(z)=0.
\tag{10}
\]
The top coefficient of (5) is
\[
q_n=\mathbb EW^n/r^n>0.
\]
Equation (6), evaluated at \(\tau=r\), shows \(q_{n-1}=0\). For each integer \(0\le j\le n-2\), coefficient comparison at \(z^j\) in (10) yields
\[
(n-j)(a+j)q_j=
(1-r)(j+2)(j+1)q_{j+2}
+(2-r)(n-1-j)(j+1)q_{j+1}.
\tag{11}
\]
Because \(0<r<1\), every coefficient on the right is nonnegative. The coefficient of \(q_{j+2}\) is strictly positive, and the denominator on the left is positive. At \(j=n-2\), \(q_n>0\) gives \(q_{n-2}>0\). Descending successively, \(q_{n-3},q_{n-4},\ldots,q_0\) are strictly positive. (For \(n=2\), the first step gives \(q_0>0\); for \(n=1\), (5) simply equals \(z\).) Therefore all coefficients in (5) are nonnegative and sum to \(Q(1)=1\); they constitute a legitimate parent distribution and yield \(X_n\stackrel d=r_n\circ Z_n\). Combined with step 1 this establishes (1)–(3).

**3. Exact support, uniqueness, other admissible parameters.** Every smaller probability is ruled out by (6). Every \(\tau\in[r_n,1]\) is admissible by composing Bernoulli thinning of \(Z_n\) first with probability \(r_n/\tau\), then with probability \(\tau\). The pgf inversion in step 1 shows uniqueness of the parent distribution for each fixed positive thinning probability. The strict induction gives the precise boundary support.

**4. Top atom and limiting strength.** The coefficient of \(z^n\) in (5) equals \(r_n^{-n}\mathbb EW^n\), while \(\Pr(X_n=n)=\mathbb EW^n\). Finally,
\[
1-r_n=\frac{b}{a+b+n-1},
\]
so \(n(1-r_n)\to b\) and \(r_n^{-n}\to e^b\). This proves (4).

## Verification
The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It checks 162 distinct combinations: nine positive rational beta-shape pairs and every integer sample size from 1 through 18. For each case it independently computes the forced parent coefficients using beta moments, compares those coefficients to the descending recurrence (3), checks nonnegativity and the exact missing \(n-1\) coefficient, reconstructs the original beta-binomial mass function by thinning, and detects a negative parent coefficient at a strictly smaller thinning probability.

For \(a=2\), \(b=3\), \(n=4\) it also verifies
\[
r_4=\frac58,\qquad
(q_0,q_1,q_2,q_3,q_4)=
\frac1{4375}(471,704,1152,0,2048).
\]
Run with `python3 verify.py`. A successful run prints `VERIFY_OK exact_cases=162 beta23_n4_threshold=5/8 hole=0 support=4`.

The finite computations verify concrete algebraic cases, not the universal quantifiers: the proof above supplies the latter through an exact polynomial differential equation and coefficient induction.

## Relationship to prior work
Kella and Löpker's *On binomial thinning and mixing* defines \(\rho\) for count laws and \(\sigma_n\) for binomial mixtures. Their Theorem 19 expresses the latter as a maximum over positive roots of several signed-moment polynomials; their Example 10 computes the special uniform-mixing case \(W\sim\mathrm{Beta}(1,1)\), obtaining \(n/(n+1)\), and their subsequent remark describes the missing penultimate parent atom and limiting inflation \(e\). The present theorem **does not claim** to originate their general root theorem or their uniform result. It instead evaluates the maximum root explicitly for every positive pair of beta shapes, proves that the penultimate root dominates throughout this continuum, and constructs the unique minimal parent by a positive descending recurrence. The new \(e^b\) asymptotic specializes to their \(e\).

Peyhardi's *On quasi Pólya thinning operator* studies generalized beta-binomial/quasi-Pólya thinning kernels and distributional closure. Jones's *Duals of convolution thinned relationships* analyzes associated convolution-thinning dualities and beta-binomial identities. Those operations are not the fixed-parameter **ordinary independent Bernoulli** de-thinning minimum studied here. The precise comparison is of operators and implication: a beta-binomial thinning identity under a random, count-dependent kernel cannot by itself furnish the threshold or positivity of the forced ordinary-thinning parent.

## Limitations
The formula is limited to beta mixing, finite sample size, and ordinary homogeneous Bernoulli thinning. It does not identify the dominant signed-moment root for arbitrary non-beta mixtures, and it is not a theorem about a random beta thinning probability. The parent law need not itself be a beta-binomial distribution. The recurrence produces probabilities exactly but does not provide a closed elementary expression for every parent atom.

Despite targeted checks, older literature on dilation, thinning indices, or Pólya count inversion may contain an equivalent formulation not captured by terminology-based searches. No claim of an independent audit is made.

## References
1. O. Kella and A. Löpker, *On binomial thinning and mixing*, arXiv:2202.10296v1 (first posted 21 February 2022); *Indagationes Mathematicae* 34 (2023), 1121–1145. DOI: 10.1016/j.indag.2022.09.003. Relevant: Theorem 19, Example 10, Remark 18; primary MSC2020 60E05.
2. J. Peyhardi, *On quasi Pólya thinning operator*, *Brazilian Journal of Probability and Statistics* (2023). DOI: 10.1214/23-BJPS585. Relevant: convolution/quasi-Pólya kernels and beta-binomial families.
3. M. C. Jones, *Duals of convolution thinned relationships*, *Statistica Neerlandica* (2024). DOI: 10.1111/stan.12337. Relevant: beta-binomial/quasi-Pólya thinning dualities and operator distinctions.
