# The exact price transition for fastest mixing on a five-cycle

## Finding

For the five-cycle on vertices \(0,1,2,3,4\), assign nonnegative conductances \(w_{01},w_{12},w_{23},w_{34},w_{40}\) to its edges. The four path edges have unit prices, and the closing edge \(\{4,0\}\) has price \(t>0\). Impose the exact budget
\[
w_{01}+w_{12}+w_{23}+w_{34}+t w_{40}=1.
\]
Write \(L(w)\) for the symmetric weighted graph Laplacian and \(\lambda_2(L(w))\) for its second-smallest eigenvalue (with eigenvalues counted with multiplicity). The following theorem determines the maximum and **every** maximizing weight vector, including the transition boundary.

**Theorem (one-priced five-cycle).** Put \(u_0=\sqrt{2/5}\). For \(0<t<16\), let \(u\) be the unique number in \((u_0,4/5)\) such that
\[
t=\frac{(5u-4)(5u-2)(5u^2-6u+2)^2}
{(u-1)(2u-1)(5u-3)^2}.
\]
Define
\[
B=\frac{2u-1}{5u-3},\qquad
Q=\frac{(2u-1)^2}{5u^2-6u+2},\qquad
\Lambda=\frac{1}{2u+2B+tQ}.
\]
Then the unique maximizer is
\[
(w_{01},w_{12},w_{23},w_{34},w_{40})
=(u\Lambda,B\Lambda,B\Lambda,u\Lambda,Q\Lambda),
\qquad \max_w\lambda_2(L(w))=\Lambda.
\]
For \(t>16\), the unique maximizer is
\[
(w_{01},w_{12},w_{23},w_{34},w_{40})=(1/5,3/10,3/10,1/5,0),
\qquad\max_w\lambda_2(L(w))=1/10.
\]
For \(t=16\), the complete set of maximizers is the nontrivial closed line segment
\[
\begin{split}
&w_{40}=q,\\
&w_{01}=w_{34}=1/5-4q,\qquad w_{12}=w_{23}=3/10-4q,\\
&0\le q\le\frac1{20}-\frac{\sqrt{10}}{200},
\end{split}
\qquad\max_w\lambda_2(L(w))=1/10.
\]
The maximizing spectral gap has multiplicity exactly two for \(0<t<16\); at \(t=16\) it has multiplicity two only at the positive endpoint of the maximizing segment, and otherwise is simple. The high-price optimum has a simple spectral gap.

In particular, there is a discontinuous change in uniqueness at the sharp price \(16\): below it, the expensive edge carries strictly positive rate; above it, the edge is deleted; at the transition, deletion and a continuum of positive allocations are equally optimal. The equal-price special case \(t=1\) has all five rates \(1/5\), with \(\Lambda=(5-\sqrt5)/10\).

## Assumptions and scope

All graph vertices have unit stationary mass; rates are symmetric and may be zero. The only data are the graph \(C_5\), one positive relative edge price \(t\), and a unit linear resource constraint. All conclusions are exact for every real \(t>0\), rather than numerical approximations or asymptotic claims. This is the continuous-time symmetric Markov-process spectral-gap objective, **not** the different discrete-time optimization of the second-largest eigenvalue modulus. Results about unpriced rings, arbitrary-price paths, and the general semidefinite programming formulation are prior art [1–3].

## Proof

**1. Reflection blocks and explicit interior candidate.** Consider the reflection-symmetric weights \(w_{01}=w_{34}=a\), \(w_{12}=w_{23}=b\), \(w_{40}=q\). The nonzero even-reflection eigenvalues are the roots of
\[
\ell^2-(2a+3b)\ell+5ab=0,
\]
and the two odd-reflection eigenvalues are the roots of
\[
\ell^2-(2a+b+2q)\ell+ab+2q(a+b)=0.
\]
These identities follow by restricting \(L\) to the spaces of vectors \((x,y,z,y,x)\) and \((x,y,0,-y,-x)\). Set \(a=u\Lambda\), \(b=B\Lambda\), \(q=Q\Lambda\), with \(u,B,Q,\Lambda\) as in the theorem. Substitution makes \(\Lambda\) a root in **both** nonconstant reflection sectors; the two corresponding centered eigenvectors are
\[
e=(1,1-1/u,2/u-4,1-1/u,1),\qquad
 o=(1,R,0,-R,-1),
\]
where
\[
R=\frac{u(5u-3)}{5u^2-6u+2}.
\]
Indeed, direct substitution into the five Laplacian equations gives \(L e=\Lambda e\) and \(L o=\Lambda o\). The two remaining eigenvalues, divided by \(\Lambda\), are respectively
\[
5uB,\qquad 2u+B+2Q-1.
\]
Both are strictly greater than one for \(u_0<u<4/5\), as proved below. Thus \(\lambda_2=\Lambda\) is double.

**2. The defining parameter exists and is unique.** Let
\[
F(u)=\frac{(5u-4)(5u-2)(5u^2-6u+2)^2}
{(u-1)(2u-1)(5u-3)^2},
\]
whose denominator is nonzero on \([u_0,4/5]\). Direct evaluation yields \(F(u_0)=16\) and \(F(4/5)=0\). Its derivative has the sign of the polynomial
\[
H(u)=2500u^6-10125u^5+16575u^4-14100u^3+6600u^2-1620u+164,
\]
because
\[
F'(u)=\frac{(5u^2-6u+2)H(u)}
{(u-1)^2(2u-1)^2(5u-3)^3}.
\]
Here \(5u^2-6u+2>0\) for every real \(u\). To certify \(H<0\), write \(u=(3+z)/5\), with \(0\le z\le1\). The coefficients of \(H((3+z)/5)\) in the degree-six Bernstein basis \(\binom6jz^j(1-z)^{6-j}\), in ascending order \(j=0,\ldots,6\), are exactly
\[
(-4/25,-11/50,-31/125,-29/125,-24/125,-6/25,-12/25).
\]
Every basis polynomial is nonnegative, so \(H<0\) throughout \([3/5,4/5]\) and in particular throughout \([u_0,4/5]\). The required solution \(u\) therefore exists uniquely for each \(0<t<16\).

**3. The candidate's other eigenvalues are larger.** On \([u_0,4/5]\), the denominators of \(B\) and \(Q\) are positive. The expression
\[
5uB-1=\frac{10u^2-10u+3}{5u-3}
\]
is positive because the quadratic numerator has negative discriminant and positive leading coefficient. Moreover,
\[
2u+B+2Q-2=\frac{50u^4-90u^3+65u^2-24u+4}
{(5u-3)(5u^2-6u+2)}.
\]
The degree-four numerator, after \(u=(3+z)/5\), has Bernstein coefficients
\[
(1/25,1/25,17/150,8/25,4/5),
\]
all strictly positive. This proves the claimed spectral ordering and identifies the true \(\lambda_2\).

**4. A sharp two-dimensional global dual certificate.** Define two scalars
\[
C_o=t/4,\qquad
C_e=u^2\left[1-\frac t4(1-R)^2\right]
=-\frac{u^2(5u^2-2)(5u^2-6u+2)}
{4(u-1)(2u-1)(5u-3)^2}.
\]
As \(u_0<u<4/5<1\), both are strictly positive. Set \(X=C_e ee^{\mathsf T}+C_o oo^{\mathsf T}\). This is a positive-semidefinite matrix and \(X\mathbf1=0\). Its squared Gram distances are exactly the five edge prices:
\[
X_{ii}+X_{jj}-2X_{ij}=1
\quad\text{on each path edge},\qquad
X_{00}+X_{44}-2X_{04}=t.
\]
The identities reduce to the three scalar relations
\[
\frac{C_e}{u^2}+C_o(1-R)^2=1,\quad
\frac{C_e(5u-3)^2}{u^2}+C_oR^2=1,\quad 4C_o=t,
\]
which hold by direct rational substitution.

For an **arbitrary** nonnegative feasible five-edge allocation \(\widetilde w\), without assuming reflection symmetry, the spectral variational inequality and the unit cost budget yield
\[
\lambda_2(L(\widetilde w))\,\operatorname{tr}X
\le \operatorname{tr}(X L(\widetilde w))
=\sum_{ij\in E}\widetilde w_{ij}(X_{ii}+X_{jj}-2X_{ij})=1.
\]
For our candidate, both \(e\) and \(o\) are \(\Lambda\)-eigenvectors, so equality holds and \(\operatorname{tr}X=1/\Lambda\). Hence \(\Lambda\) is the **global** maximum.

**5. Interior uniqueness without a symmetry assumption.** Any other optimizer \(\widetilde w\) must attain equality in the preceding trace inequality. Because \(C_e,C_o>0\), both \(e\) and \(o\) must be \(\Lambda\)-eigenvectors of \(L(\widetilde w)\). The middle vertex's odd eigenvalue equation forces \(\widetilde w_{12}=\widetilde w_{23}\); its even equation then gives their common value \(B\Lambda\). The even eigenvalue equations at vertices \(0\) and \(4\) fix \(\widetilde w_{01}=\widetilde w_{34}=u\Lambda\); finally the odd equation at vertex \(0\) fixes \(\widetilde w_{40}=Q\Lambda\). Thus **every** optimizer is the given one, not just every symmetric optimizer.

**6. The high-price boundary and all boundary optimizers.** Define the centered vector \(v=(-2,-1,0,1,2)\), which has squared norm \(10\). Its differences have squared magnitude \(1\) on all four path edges and \(16\) on the closing edge. The Rayleigh principle therefore yields for every feasible allocation
\[
\lambda_2(L(w))\le\frac{v^{\mathsf T}L(w)v}{10}
=\frac{1+(16-t)w_{40}}{10}.
\]
For \(t>16\), positive closing-edge weight gives a strict upper bound below \(1/10\). The path allocation \((1/5,3/10,3/10,1/5,0)\) has \(L(w)v=v/10\) and all other nonzero eigenvalues strictly above \(1/10\); it thus attains the bound. Any other optimum must have closing weight zero and \(v\) as a \(1/10\)-eigenvector; its four vertex difference equations uniquely recover those four path weights.

At \(t=16\), every optimizer again must have \(L(w)v=v/10\), because the Rayleigh bound is saturated. Solving the five equations gives the **necessary** family
\[
w_{40}=q,\quad w_{01}=w_{34}=1/5-4q,\quad w_{12}=w_{23}=3/10-4q.
\]
Nonnegativity restricts \(0\le q\le1/20\). The odd-reflection eigenvalues are then \(1/10\) and \(3/5-10q\), with the second strictly greater than \(1/10\) for \(q<1/20\). The even-reflection sector has quadratic characteristic expression
\[
\ell^2-(2a+3b)\ell+5ab,
\]
whose value at \(\ell=1/10\) is exactly
\[
\frac{4000q^2-400q+9}{50}.
\]
Its trace stays above \(1/5\) on the relevant nonnegative range. Consequently its smaller root is at least \(1/10\) precisely when
\[
0\le q\le \frac1{20}-\frac{\sqrt{10}}{200}.
\]
At equality the even root also equals \(1/10\), giving multiplicity two; elsewhere it is larger and the gap is simple. This proves the full optimizer segment and completes the theorem. \(\square\)

## Verification

The accompanying standalone `verify.py` uses exact SymPy arithmetic. It verifies both eigenvector identities, all five dual-distance identities, the derivative factorization, all Bernstein sign coefficients, the high-price boundary polynomial, the exact critical endpoint, and the unit-price special case. Run from a directory containing the file using `python3 verify.py`; the expected terminal output is `VERIFY_OK exact five-cycle algebra, Bernstein signs and endpoint identities`.

The proof is valid for every \(t>0\), whereas the symbolic computations verify the displayed identities and sign certificates; floating-point optimizers or sampled values are not substituted for the universal trace inequality.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis [1] established the continuous-time fastest-mixing semidefinite formulation and maximum-variance-unfolding dual. Their section 5.2 gives the arbitrary-cost path solution; section 5.3 gives the equal-price cycle solution and the general bound that optimal cycle unfoldings have dimension at most two. Those facts are **prior art**, not claimed here. Their inspected section 5.3 does not provide the one-exceptional-price five-cycle classification, its explicit sharp \(t=16\) transition, the full critical optimizer segment, or uniqueness at all noncritical prices.

Boyd, Diaconis, Parrilo, and Xiao [2] optimize the distinct **discrete-time** fastest-mixing-chain objective, including unpriced edge-transitive cycles by symmetry. That result does not imply the present heterogeneously priced continuous-time optimizer classification. Fiedler [3] addresses maximum Laplacian connectivity and its tree special cases rather than this priced ring formula.

## Limitations

The theorem is specific to a five-cycle with exactly one edge price distinct from the other four. It does not classify arbitrary edge-price vectors, larger cycles, the discrete-time SLEM optimization, nonsymmetric transition rates, or nonuniform stationary distributions. A prior work with an equivalent C5 special case not surfaced by the searches remains possible; absence from the inspected papers is not a proof of universal novelty. No independent validation is asserted.

## References

[1] J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review **48** (2006), 681–699, DOI: 10.1137/S0036144504443821; publicly available author PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published electronically 2006-11-02).

[2] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792–819, DOI: 10.1137/070689413; author PDF: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.

[3] M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra **26** (1990), 85–106; mentioned and precisely distinguished in [1, section 5.2].
