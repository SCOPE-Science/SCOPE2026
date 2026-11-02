# Exact active-edge allocation on a five-cycle with one priced link

## Finding

Consider the five-cycle \(C_5\) on vertices \(0,1,2,3,4\). Let the path edges \(01,12,23,34\) each have unit price per unit conductance, and let the closing edge \(40\) have price \(q\). Choose all five nonnegative edge conductances independently under a budget \(B>0\), maximizing the second-smallest eigenvalue \(\lambda_2(L)\) of the ordinary weighted graph Laplacian. **For every \(0<q<16\), the unique global optimum has five strictly positive conductances and admits the following explicit one-variable algebraic parametrization.**

There is a unique \(a\in(\sqrt{2/5},4/5)\) satisfying
\[
q=\frac{(5a-4)(5a-2)(5a^2-6a+2)^2}
{(a-1)(2a-1)(5a-3)^2}=:Q(a).
\]
Define
\[
b=\frac{2a-1}{5a-3},\qquad
 t=\frac{(2a-1)^2}{5a^2-6a+2},\qquad
 C=2a+2b+qt.
\]
The optimum is uniquely attained at
\[
(w_{01},w_{12},w_{23},w_{34},w_{40})
  =\frac{B}{C}(a,b,b,a,t),
\qquad \max\lambda_2(L)=\frac{B}{C}.
\]
This uniqueness is **unrestricted**: the conductances were not required a priori to respect graph reflection. At \(q=25/16\) the exact normalized design is \((a,b,b,a,t)=(7/10,4/5,4/5,7/10,16/25)\), its normalized cost is \(C=4\), and its optimal gap is \(B/4\). The edge-price interval is exact: the solution approaches the path-edge-screening boundary \(q=16\) as \(a\downarrow\sqrt{2/5}\), and tends to the zero-price endpoint as \(a\uparrow4/5\). In particular,
\[
\lim_{q\downarrow0}\max\lambda_2(L)=\frac{5B}{14},\qquad
\lim_{q\uparrow16}\max\lambda_2(L)=\frac{B}{10}.
\]
The endpoints themselves are **not** included in the uniqueness claim.

## Assumptions and scope

The graph is a simple undirected five-cycle; \(L_{ii}\) equals the sum of incident edge conductances and \(L_{ij}=-w_{ij}\) on edges. The stationary masses are uniform, and the objective is continuous-time spectral-gap maximization, not discrete-time second-largest-eigenvalue-modulus minimization. The independent conductances are nonnegative and cost \(w_{01}+w_{12}+w_{23}+w_{34}+qw_{40}\le B\). Every assertion in this finding holds for arbitrary real \(B>0\) and \(q\in(0,16)\). The normalization \(\lambda_2=1\) used below is justified by the positive homogeneity of the Laplacian spectrum.

## Proof

**1. Reflection decomposition and spectral equations.** For a reflection-symmetric normalized design \((a,b,b,a,t)\), the nonconstant even and odd subspaces of reflection \(0\leftrightarrow4\), \(1\leftrightarrow3\), \(2\leftrightarrow2\) have two nonzero eigenvalues each. The lower eigenvalues are
\[
\lambda_e=\frac{2a+3b-\sqrt{(2a+3b)^2-20ab}}2,
\qquad
\lambda_o=\frac{2a+b+2t-\sqrt{(b-2t)^2+4a^2}}2.
\]
The condition that both lower eigenvalues equal \(1\) is equivalent, respectively, to
\[
1-(2a+3b)+5ab=0,
\qquad (a+2t-1)(a+b-1)-a^2=0.
\]
Solving those identities gives exactly \(b=(2a-1)/(5a-3)\) and \(t=(2a-1)^2/(5a^2-6a+2)\). On \(\sqrt{2/5}<a<4/5\), the numbers \(a,b,t\) are positive. The other eigenvalue in each two-dimensional nonconstant block is the respective trace minus \(1\). Both traces are strictly greater than \(2\): indeed \(a>\sqrt{2/5}>3/5\), \(b>3/5\), and \(t>0\), so \(2a+3b>3\) and \(2a+b+2t>9/5\), with the stronger strict lower bound \(2a+b+2t>2\) following from \(a>\sqrt{2/5}\), \(b>3/5\), and \(t\ge 1/2-\sqrt{10}/20>3/10\). Thus the resulting full Laplacian has \(\lambda_2=1\) with multiplicity exactly two.

**2. The price function is strictly monotone.** Let
\[
D_0(a)=5a^2-6a+2,\quad
P(a)=2500a^6-10125a^5+16575a^4-14100a^3
        +6600a^2-1620a+164.
\]
Direct differentiation yields
\[
Q'(a)=\frac{D_0(a)P(a)}{(a-1)^2(2a-1)^2(5a-3)^3}.
\]
Here \(D_0(a)>0\), so the sign is that of \(P(a)\). To prove its negativity without numerical root-finding, put \(z=5a-3\in[0,1]\). The polynomial has the Bernstein representation
\[
P((3+z)/5)=\sum_{j=0}^6\binom6j\beta_j z^j(1-z)^{6-j},
\quad (\beta_0,\ldots,\beta_6)=
\left(-\frac4{25},-\frac{11}{50},-\frac{31}{125},
-\frac{29}{125},-\frac{24}{125},-\frac6{25},-\frac{12}{25}\right).
\]
All coefficients are strictly negative. Hence \(Q'(a)<0\) throughout the domain; continuity and direct endpoint evaluation give
\(Q(\sqrt{2/5})=16\), \(Q(4/5)=0\). Thus precisely one \(a\) exists for each \(0<q<16\).

**3. An exact dual certificate.** Write
\[
E=10a^2-10a+3>0,\qquad
D=D_0(a)^2+a^2(5a-3)^2>0.
\]
Along the normalized two-branch intersection, the spectral derivatives with respect to the paired conductance variables are
\[
\begin{array}{lll}
\partial_a\lambda_e=1/E,&\partial_b\lambda_e=(5a-3)^2/E,&\partial_t\lambda_e=0,\\
\partial_a\lambda_o=(3a-2)^2/D,&\partial_b\lambda_o=a^2(5a-3)^2/D,&\partial_t\lambda_o=2D_0(a)^2/D.
\end{array}
\]
Define two positive numbers
\[
\alpha=-\frac{(5a^2-2)D_0(a)E}
{2(a-1)(2a-1)(5a-3)^2},\qquad
\beta=\frac{(5a-4)(5a-2)D}
{2(a-1)(2a-1)(5a-3)^2}.
\]
Their positivity is immediate from the open interval: \(5a^2-2>0\), \(a-1<0\), and \(5a-4<0\). Exact rational simplification establishes the three identities
\[
\alpha\partial_a\lambda_e+\beta\partial_a\lambda_o=2,
\quad\alpha\partial_b\lambda_e+\beta\partial_b\lambda_o=2,
\quad\beta\partial_t\lambda_o=q,
\]
plus \(\alpha+\beta=2a+2b+qt=C\).

Let \(u\) and \(v\) be unit even and odd eigenvectors for eigenvalue \(1\) at this design. They can be taken proportional to
\[
 u=\left(1,\frac{a-1}{a},
 \frac{2b(a-1)}{a(2b-1)},\frac{a-1}{a},1\right),
\quad
 v=\left(1,\frac{a}{a+b-1},0,
 -\frac{a}{a+b-1},-1\right).
\]
The derivative identities are exactly the edgewise equalities
\[
\alpha(u_i-u_j)^2+\beta(v_i-v_j)^2
=\begin{cases}1,&ij\in\{01,12,23,34\},\\ q,&ij=40.\end{cases}
\]
Here the vectors are normalized before taking differences, and the variables \(a,b\) in the derivative identities represent two edges apiece. For **any** other nonnegative conductances \(w'\) with \(\lambda_2(L(w'))\ge1\), the min–max principle and the exact edgewise equalities therefore imply
\[
\begin{aligned}
\mathrm{cost}(w')
&=\alpha u^{\mathsf T}L(w')u+\beta v^{\mathsf T}L(w')v\\
&\ge\alpha+\beta=C.
\end{aligned}
\]
Thus the candidate minimizes total cost at prescribed gap \(1\), **against arbitrary independent edge allocations**, and homogeneity proves the stated budget-normalized optimum.

**4. Global uniqueness, including asymmetric alternatives.** If another design \(w'\) achieved the same optimal gap under the budget, rescale it to gap \(1\). It then attains equality above; because \(\alpha,\beta>0\), both \(u\) and \(v\) have Rayleigh quotient exactly \(1\). Since the symmetric matrix \(L(w')\) is at least the identity on the mean-zero subspace, the two vectors must be actual eigenvectors with eigenvalue \(1\). The even vector satisfies \(u_0=u_4\), \(u_1=u_3\), with \(u_0\ne u_1\) and \(u_1\ne u_2\). Its eigenvector equations at vertices \(0,4\) uniquely fix \(w'_{01}=w'_{34}=a\), and at vertices \(1,3\) uniquely fix \(w'_{12}=w'_{23}=b\). Since \(v_0=-v_4\ne0\), its equation at vertex \(0\) then uniquely fixes \(w'_{40}=t\). This proves unrestricted uniqueness. The endpoint limits follow by substituting \(a=4/5\) and \(a=\sqrt{2/5}\) into the continuous formulas.

## Verification

A standalone verifier is supplied in `verify.py`. It symbolically checks the two spectral equations, both full five-vertex eigenvector identities, every edgewise normalized dual equality, the cost identity, the derivative factorization, and all seven exact Bernstein coefficients, without floating-point arithmetic. It checks the nontrivial exact rational instance \(q=25/16\). Independent floating-point Laplacian eigensolvers additionally check both equal low eigenvalues for ten prices and compare 1,500 independently sampled feasible allocations against the proven value, giving 1,520 numerical supplementary checks. These finite checks are not used as a substitute for the polynomial and dual proofs.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis (2006, Sections 3–5) formulate the same continuous-time weighted spectral-gap maximization as a semidefinite program and derive its maximum-variance-unfolding dual. Their Section 5.3 resolves equal-price cycles and proves that general cycles have dual dimension at most two; it explicitly treats arbitrary edge prices as more complicated, without giving the present five-cycle closed algebraic allocation. Boyd, Diaconis, and Xiao (2004) study **discrete-time** second-largest-eigenvalue-modulus minimization, not this budget-priced continuous-time gap. Prior edge-screening results identify the critical closing-edge price \(q=16\) for a five-cycle with four unit path prices; that already-known threshold is not claimed as new. The present result gives the previously unspecified unique all-edge-optimal allocation and value at **every** strictly subcritical price \(0<q<16\), including all asymmetric competitors and the exact monotone parameter law. General semidefinite solvers, duality, and generic eigenvalue formulas are acknowledged as prior methods.

## Limitations

The theorem concerns exactly five vertices, four identical unit prices and one exceptional closing-edge price; it is not a general arbitrary-price or arbitrary-mass cycle theorem. It excludes the transition \(q=16\) and the endpoint \(q=0\), where the uniqueness structure changes, and makes no claim about discrete-time transition-matrix SLEM or all-purpose mixing-time constants. Published sources were inspected for equivalent/stronger coverage; historical specialist spectral-optimization papers not fully accessible remain a priority risk.

## References

1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: https://doi.org/10.1137/S0036144504443821 ; author-hosted complete PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf . Verified electronic publication date: 2006-11-02.
2. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, https://doi.org/10.1137/S0036144503423264 ; complete PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf .
3. M. Fiedler, *Some minimax problems for graphs*, Discrete Mathematics 121 (1993), 65–74. Original complete text not inspected; cited as a possible broad methodological predecessor, not as evidence of noncoverage.
