# Sharp Turán mass and optimizer geometry of radius-three Boolean Hamming balls
## Finding
Let \(d\ge3\), \(G=\mathbb F_2^d\), and \(B_3=\{x\in G:|x|\le3\}\), where \(|x|\) is Hamming weight. For all complex-valued positive-definite functions \(f:G\to\mathbb C\) with \(f(0)=1\) and \(\operatorname{supp}f\subseteq B_3\), the exact maximum, with **counting measure**, is
\[
\boxed{\mathcal T_d(B_3)=\sup_f\sum_{x\in G}f(x)=\begin{cases}2d+2,&d\text{ odd},\\2d,&d\text{ even}.\end{cases}}
\]
For **every odd \(d\ge5\)** all maximizing functions are classified as follows. Write the unnormalized Walsh transform as
\[
F(y)=\widehat f(y)=\sum_{x\in G}f(x)(-1)^{x\cdot y},\quad
s_i=(-1)^{y_i},\quad S=\sum_{i=1}^d s_i.
\]
Then \(f\) is a maximizer if and only if there exist real numbers \(b_i\ge0\) with \(\sum_i b_i=1/(d-1)\) such that
\[
\boxed{F(y)=(S^2-1)\sum_{i=1}^d b_i(1+s_i).}
\]
Different \((b_i)\) give different functions. Thus the complete odd-dimensional optimizer set, for \(d\ge5\), is a \((d-1)\)-simplex; its \(d\) vertices are nonradial. For \(d=3\) the unique optimizer is \(f\equiv1\) because \(B_3=G\).

For **every even \(d\ge4\)** all *permutation-invariant (radial)* maximizing functions are classified by one parameter \(\alpha\in[-2,2]\):
\[
\boxed{F(y)=\frac{(S+d)S(S-\alpha)}{d(d-\alpha)}.}
\]
These form an interval of distinct radial maximizers. No complete classification of the nonradial even-dimensional maximizers is claimed.

## Assumptions and scope
A function \(f\) is positive definite when each matrix \((f(u-v))_{u,v\in G}\) is positive semidefinite, equivalently \(\widehat f(y)\ge0\) for every \(y\in G\). On this exponent-two group, every positive-definite function is real. The Walsh transform is unnormalized and the inverse transform is
\[
f(x)=2^{-d}\sum_{y\in G}\widehat f(y)(-1)^{x\cdot y}.
\]
The objective is the unnormalized sum \(\sum_x f(x)=F(0)\); this differs by the factor \(2^d\) from the integral under normalized Haar measure. Coordinates are labeled, and no radiality is assumed in the odd-dimensional optimizer classification.

## Proof
**Upper bound by explicit nonnegative spectral certificates.** Average any eligible \(f\) over permutations of the \(d\) coordinates. Positivity, support, \(f(0)\), and total mass are preserved; the averaged function is radial. Write \(a_j=f(x)\) when \(|x|=j\), with \(a_0=1\), and let \(F_k\) be its Walsh value at any frequency of weight \(k\). With \(S=d-2k\), Krawtchouk summation gives
\[
F_k=1+a_1 S+a_2\frac{S^2-d}{2}
+a_3\frac{S^3-(3d-2)S}{6}.
\]
A direct coefficient comparison in this cubic yields the **identities**, valid for every eligible radial \(f\),
\[
F_0+dF_{(d-1)/2}+dF_{(d+1)/2}+F_d=2(d+1)
\quad(d\text{ odd}),
\]
\[
F_0+2(d-1)F_{d/2}+F_d=2d
\quad(d\text{ even}).
\]
All terms except \(F_0\) are nonnegative, proving the claimed bounds for radial and hence arbitrary functions.

**Sharpness and explicit construction.** For odd \(d\), set
\[
F(y)=\frac{(S+d)(S^2-1)}{d(d-1)}.
\]
Every allowable \(S\) is odd with \(-d\le S\le d\), so \(F\ge0\). For even \(d\), set
\[
F(y)=\frac{(S+d)S(S+2)}{d(d+2)}.
\]
Every allowable \(S\) is even, and the signs of \(S\) and \(S+2\) agree or one is zero, so again \(F\ge0\). Each expression is a polynomial of total Walsh degree at most three, hence its inverse transform is supported in \(B_3\). For a sum \(S\) of \(d\) independent uniform Rademacher signs,
\[
\mathbb ES=\mathbb ES^3=0,\qquad \mathbb ES^2=d.
\]
Consequently \(2^{-d}\sum_yF(y)=1\), exactly the normalization \(f(0)=1\). The values at \(S=d\) attain \(2(d+1)\) and \(2d\), respectively.

**Complete equality classification when \(d\) is odd.** If equality holds, the odd upper identity and the nonnegativity of each original Walsh value imply that \(F\) vanishes at every frequency with \(S=1\), \(S=-1\), or \(S=-d\). The implication follows because each radial Fourier value is the average of nonnegative original values over that full frequency layer.

We use an elementary two-slice divisibility lemma. For odd \(d=2k+1\ge7\), every multilinear real polynomial \(P(x_1,\ldots,x_d)\) of degree at most three which vanishes on all binary vectors of weights \(k\) and \(k+1\) has the form
\[
P(x)=(w-k)(w-k-1)H(x),\qquad w=\sum_i x_i,
\]
with \(H\) affine linear. To prove it, let \(V_r\) be the space of multilinear polynomials of degree at most \(r\), of dimension \(\sum_{j=0}^r\binom dj\). The restrictions of degree-\(r\) squarefree monomials to the weight-\(m\) slice are linearly independent whenever \(r\le\min(m,d-m)\): indeed, for a purported dependence, exchanging one element in two \(m\)-subsets gives an analogous dependence of degree \(r-1\) on the \((m-1)\)-slice of \(d-2\) variables. Induction forces coefficients of any two \(r\)-subsets differing by one exchange to be equal; connectedness of the exchange graph then forces all coefficients to be zero. On a fixed weight-\(m\) slice, every lower-degree monomial is a linear combination of degree-\(r\) monomials, by summing all degree-\(r\) supersets. Therefore the kernel of restriction \(V_r\to\{w=m\}\) has dimension \(\dim V_{r-1}\). Multiplication by \(w-m\) sends \(V_{r-1}\) into this kernel injectively for \(m\ge r\): if the product vanishes on the whole cube, its factor vanishes at weights \(0,\ldots,r-1\), and elementary coefficient induction makes that factor zero. Hence that multiplication *is* the whole kernel. Apply this first with \(r=3,m=k\), then with \(r=2,m=k+1\), to obtain the displayed factorization.

For \(d=5\), the same factorization follows by direct dimension counting: the degree-at-most-three polynomial space has dimension \(26\); evaluation on the two layers of weights \(2\) and \(3\) has rank \(20\). For every two-subset \(A\), the degree-three polynomial \(x_A(3-w)\) interpolates its indicator on layer two and vanishes on layer three. For every three-subset \(B\), \(x_B\) interpolates its indicator on layer three and vanishes on layer two. Thus the kernel dimension is six, exactly the dimension of \((w-2)(w-3)\) times affine polynomials; these products are linearly independent because their affine factors are determined by weights zero and one.

Replace the Boolean variables by \(x_i=(1+s_i)/2\). The lemma yields
\[
F(s)=(S^2-1)\left(c_0+\sum_i b_i s_i\right).
\]
The additional zero at \(s_1=\cdots=s_d=-1\) implies \(c_0=\sum_i b_i\), giving the claimed form. For any fixed \(i\), choose \(s_i=1\) and all other signs \(-1\). Since \(d\ge5\), \(S=-(d-2)\) has \(S^2-1>0\), and nonnegativity forces \(b_i\ge0\). Conversely all nonnegative \(b_i\) make \(F\ge0\). The Walsh-average identity
\[
\mathbb E_s\big[(S^2-1)(1+s_i)\big]=d-1
\]
shows that normalization is exactly \(\sum_i b_i=1/(d-1)\). The value at all positive signs is then \(2(d+1)\). Evaluating at each sign vector with exactly one positive sign determines its \(b_i\), so this parametrization is injective. When \(d=3\), \(B_3=G\) and the mass bound \(\sum f\le2^d\) has the unique equality case \(f\equiv1\).

**Complete radial equality classification when \(d\) is even.** An extremal radial cubic \(F(S)\) has zeros at \(S=0\) and \(S=-d\) by the even upper identity, so it factors as \((S+d)S(AS+B)\). Nonnegativity at \(S=2,-2\) forces \(-2A\le B\le2A\) and therefore \(A>0\). Put \(\alpha=-B/A\in[-2,2]\). The Walsh average of \((S+d)S(S-\alpha)\) is \(d(d-\alpha)\), forcing the displayed normalization. Conversely every \(\alpha\in[-2,2]\) gives a nonnegative cubic at all even \(S\) from \(-d\) to \(d\), proving necessity and sufficiency.

## Verification
The accompanying `check_hamming_radius3.py` uses exact fractions. For dimensions \(3\) through \(11\), it inverts all proposed Walsh spectra, checks nonnegativity, the precise Hamming-support cutoff, normalization and the optimum, and checks both dual identities in the full degree-three Krawtchouk basis. It tests all odd-dimensional simplex vertices and three even-dimensional radial parameters. Exact modular rank tests of the odd equality-slice matrices independently confirm nullities \(5,7,9\) in dimensions \(5,7,9\). Output:

`EXACT_FOURIER_VERIFY_OK dimensions=3..11 constructions= 49`

`EXACT_MODULAR_KERNEL_RANK_OK dimension= 5 rank= 21 nullity= 5`

`EXACT_MODULAR_KERNEL_RANK_OK dimension= 7 rank= 57 nullity= 7`

`EXACT_MODULAR_KERNEL_RANK_OK dimension= 9 rank= 121 nullity= 9`

`VERIFY_OK`

These finite computations are a check on the formulas and the divisibility lemma, not a replacement for the unrestricted proof.

## Relationship to prior work
Berdysheva and Révész, *Delsarte's Extremal Problem and Packing on Locally Compact Abelian Groups* (arXiv:1904.03614), establish the general positive-definite Turán/Delsarte framework and packing inequalities. Their full HTML text was compared; no radius-three Boolean Hamming-ball exact value or optimizer classification was found. Krenedits and Révész, *Carathéodory–Fejér type extremal problems on locally compact Abelian groups* (arXiv:1304.0071), treat pointwise rather than total-mass optimization and formulate general positive-definite reductions. A published exact solution for the **weight-two shell** \(\{0\}\cup\{|x|=2\}\) gives a different support problem with mass \(d\) or \(d+1\); it does not determine the radius-three ball's complete odd-dimensional simplex or even-dimensional radial interval. The present problem includes Hamming weights one and three, and the odd-dimensional extremizer geometry changes from uniqueness on the shell to a full simplex on the ball.

## Limitations
The all-dimensional Turán maximum and all odd-dimensional optimizers are proved; for even dimensions only the radial optimizer family is classified. The claim is about finite binary groups and counting measure; it gives neither a coding-theory packing optimum nor a classification for Hamming balls of other radii. Older coding-theory or association-scheme work could conceivably contain the numerical constant or an equivalent general LP reduction; no claim of bibliographic exhaustiveness or independent certification is made.

## References
1. E. E. Berdysheva and S. Gy. Révész, *Delsarte's Extremal Problem and Packing on Locally Compact Abelian Groups*, arXiv:1904.03614v1, first public 2019-04-07; full text https://arxiv.org/html/1904.03614v4.
2. S. Krenedits and S. Gy. Révész, *Carathéodory–Fejér type extremal problems on locally compact Abelian groups*, arXiv:1304.0071, first public 2013-03-30; full text https://arxiv.org/html/1304.0071v5.
3. *Sharp Turán constant and all extremizers for the weight-two Boolean Hamming shell*, published result https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-sharp-tur-n-constant-and-all-extremizers-for-the-weight-two-bool--e912a3cb52c4/RESULT.md.
