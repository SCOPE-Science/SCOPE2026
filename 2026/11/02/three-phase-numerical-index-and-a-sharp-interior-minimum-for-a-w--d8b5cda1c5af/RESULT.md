# Three-phase numerical index and a sharp interior minimum for a weighted four-cycle

## Finding
Let \(M_r\) be the four vertices of a cycle with successive positive edge lengths \(1,1,1,r\), endowed with the shortest-path metric, and let \(X_r=\mathcal F(M_r)\) be the **real** Lipschitz-free Banach space. For every \(1\le r\le3\), its numerical index has the exact three-phase formula
\[
\boxed{\mathfrak n(X_r)=
\begin{cases}
\dfrac{r(3-r)}{3r-1},&1\le r\le5/3,\\[3pt]
\dfrac r3,&5/3\le r\le1+\sqrt2,\\[3pt]
\dfrac{r+1}{-r^2+5r-2},&1+\sqrt2\le r\le3.
\end{cases}}
\]
The **unique minimum** on this interval is \(\mathfrak n(X_{5/3})=5/9\). Thus the numerical index falls from one at the equal-edge square, then rises back to one when the length-three edge becomes metrically redundant, with phase transitions at \(5/3\) and \(1+\sqrt2\). The sharp value at each interior parameter is attained by a rank-one operator. In combination with the known complementary short-edge formula for \(0<r\le1\), this determines the index over all positive edge lengths after rescaling three edges to one.

## Assumptions and scope
All operators and spaces are over \(\mathbb R\). For \(0<r<3\), the four edges are strictly shorter than their respective alternative paths. For \(r=3\), the long edge is redundant but all four metric points remain distinct. Define the numerical radius and index by
\[
v(T)=\sup\{|f(Tx)|:\|x\|=\|f\|=1,\ f(x)=1\},\qquad
\mathfrak n(X)=\inf_{\|T\|=1}v(T).
\]
Orient the cycle and write \(v_1,v_2,v_3\) for the three normalized unit-edge molecules and \(v_4\) for the normalized length-\(r\) molecule. Then
\[
v_1+v_2+v_3+rv_4=0.
\]
Represent vectors as \(y=a v_1+b v_2+c v_3\); the quotient norm is the weighted transportation norm
\[
\|y\|=\min_{s\in\mathbb R}\bigl(|a+s|+|b+s|+|c+s|+r|s|\bigr).
\]
In these coordinates dual functionals are quadruples \(f=(f_1,f_2,f_3,f_4)\) with \(f_1+f_2+f_3+f_4=0\). Their unit ball is
\[
F_r=\{f:|f_1|,|f_2|,|f_3|\le1,\ |f_4|\le r,\ \sum_i f_i=0\},
\]
and \(f(v_4)=f_4/r\). For \(1<r<3\), its twelve extreme points consist of sign changes and permutations of the first three entries of the two patterns \((r-2,1,1,-r)\) and \((1,1,-1,-1)\). All four signed normalized edge molecules are extreme in the primal ball.

## Proof
**Step 1: Reduction to norming vertices.** As the primal ball is \(\operatorname{conv}\{\pm v_i:1\le i\le4\}\), every operator satisfies \(\|T\|=\max_i\|Tv_i\|\). The extreme-point formula for the numerical radius is
\[
v(T)=\max_{1\le i\le4}\max_{\substack{f\in\operatorname{ext}F_r\\f(v_i)=1}}|f(Tv_i)|.
\]
Indeed, a norming pair \((x,f)\) can be decomposed first into extreme primal vectors belonging to the exposed face \(f(x)=1\), then into extreme dual functionals from the corresponding norming face; the absolute evaluation is bounded by one of the resulting extreme pairs. The vertex list follows by intersecting the coordinate box with the zero-sum hyperplane: at a vertex at least three coordinate bounds are tight; if \(|f_4|=r>1\), exactly two of the first three are saturated with the same sign, leaving the third equal to \(r-2\) up to sign, whereas if \(|f_4|<r\), all first three must be saturated and their sum is \(\pm1\).

**Step 2: Two optimal domination constants.** Set
\[
K_L=\frac{-r^2+5r-2}{r+1},\quad
L_H=\frac{3r-1}{r(3-r)},\quad
K_H=\min\left\{L_H,\frac3r\right\}.
\]
For a light-edge source (say \(v_1\)), all dual vertices norm it except the two variants of the first pattern with \(f_1=\pm(r-2)\). Up to sign and permutation, the exceptional functional admits the **exact** identity
\[
(r-2,1,1,-r)=\frac{r-1}{r+1}\bigl[(1,1,r-2,-r)+(1,r-2,1,-r)\bigr]
-\frac{r(3-r)}{r+1}(1,-1,-1,1).
\]
Each of the three functionals on the right norms \(v_1\). Taking absolute values yields \(\|Tv_i\|\le K_L v(T)\) for every light \(i=1,2,3\).

For the heavy-edge source \(v_4\), the first-pattern dual vertices are already norming. To control a nonnorming second-pattern vertex \(B=(1,1,-1,-1)\), set
\[
c=\frac{r-1}{r(3-r)},\qquad d=\frac{r+1}{r(3-r)},\qquad
h_1=(2-r,-1,-1,r),\ h_2=(-1,2-r,-1,r),\ h_3=(-1,-1,2-r,r).
\]
The \(h_i\) all norm \(v_4\) and satisfy \(B=c(h_1+h_2)-dh_3\). Hence \(|B(Tv_4)|\le(2c+d)v(T)=L_Hv(T)\). Alternatively, the relation \(rv_4=-v_1-v_2-v_3\), together with \(|B(v_i)|=1\) for all three light edges, gives \(|B(Tv_4)|\le3v(T)/r\). Thus
\[
\boxed{\|T\|\le \max\{K_L,K_H\}\,v(T)}.
\]

**Step 3: Both bounds are attained by rank-one operators.** Set
\[
a=\frac{3-r}{r+1},\quad b=\frac2{r+1},\quad
y_L=a v_1+b(v_2+v_3),\quad
\varphi_L(v_1)=1,\ \varphi_L(v_2)=\varphi_L(v_3)=-\tfrac12,\ \varphi_L(v_4)=0.
\]
The quotient-norm minimum is attained at \(s=-a\), giving \(\|y_L\|=K_L\); also \(\|\varphi_L\|=1\). The five extreme norming dual vertices for \(v_1\) take values on \(y_L\) of modulus at most one, and attain one. At \(v_2,v_3\), their contribution is at most \(\|y_L\|/2<1\); at \(v_4\), it vanishes. Consequently \(T_L=\varphi_L\otimes y_L\) has \(v(T_L)=1\), \(\|T_L\|=K_L\).

For the heavy source put \(y_H=c v_1+c v_2-d v_3\) and define \(\varphi_H(v_i)=-r/3\) for \(i=1,2,3\), \(\varphi_H(v_4)=1\). The quotient norm is minimized at \(s=0\), so \(\|y_H\|=2c+d=L_H\) and \(\|\varphi_H\|=1\). The norming dual vertices for \(v_4\) evaluate \(y_H\) with modulus exactly one; each light-edge norming slice has maximum \(L_H\), witnessed by the second-pattern vertex \((1,1,-1,-1)\) up to signs. Hence
\[
\|T_H\|=L_H,\qquad v(T_H)=\max\{1,rL_H/3\},\qquad
\frac{\|T_H\|}{v(T_H)}=K_H.
\]
As every nonzero operator can be normalized to norm one, the exact numerical index is therefore
\[
\mathfrak n(X_r)=\frac1{\max\{K_L,K_H\}}.
\]

**Step 4: Comparison, phases, and endpoints.** Direct algebra shows \(K_H=L_H\) for \(r\le5/3\), while \(K_H=3/r\) for \(r\ge5/3\). For \(1<r\le5/3\), one has \(L_H\ge K_L\); for \(5/3\le r\le1+\sqrt2\), \(3/r\ge K_L\); and for \(1+\sqrt2\le r<3\), \(K_L\ge3/r\). The comparison zeros are exactly \(r=5/3\) and \(r=1+\sqrt2\), yielding the displayed three pieces. The first branch decreases strictly to \(5/9\), the second increases, and the third increases: uniqueness of the minimum follows. At \(r=1\), the dual cube-section vertices all saturate every normalized edge, so the extreme-pair formula gives \(\mathfrak n=1\). At \(r=3\), deleting the redundant heavy edge leaves a tree metric and \(X_3\cong\ell_1^3\), again of numerical index one.

## Verification
A stand-alone Python 3 checker `verify.py`, using only `fractions` and `itertools`, exhaustively enumerates the twelve dual vertices for **359 distinct rational parameters** in \(1<r<3\); it checks the two exact functional identities, both rank-one operator norms, their exact numerical radii, and supplementary domination tests. Execute `python verify.py` to obtain `VERIFY_OK rational_parameters=359 12_dual_vertices=True exact_norm_radius=True`. The full interval theorem is proved analytically above; finite computations are diagnostics, not an exhaustive proof for real parameters. The proof and checker use the same explicit quotient norm and normalized molecules.

## Relationship to prior work
Cobollo, Guirao, and Montesinos (2023) give the numerical index for the three-point (two-dimensional) Lipschitz-free spaces, not this three-dimensional four-point family. The published **short-edge** four-cycle evaluation determines \(\mathfrak n(\mathcal F(M_r))=1/(2-r)\) only for \(0<r\le1\), and explicitly leaves \(r>1\) outside its scope. The published weighted-cycle numerical-index-one characterization says the index is one for equal-edge even cycles or metrically redundant edges; it does not determine the **quantitative values below one**, the interior minimum, or the two transitions. Classical polyhedral numerical-radius methods and transportation-cost quotient representations underlie the proof but do not, by themselves, yield the three-phase evaluation. The current result fills the complementary long-edge regime.

## Limitations
The theorem treats real scalars, four distinct vertices, and a single variable edge opposite three fixed unit edges. It does not give an exact numerical-index formula for arbitrary four independent edge lengths or for complex scalars. In the interior, both sharp operators are rank one; this does not classify all minimizers. An equivalent prior derivation under a different polyhedral, transportation-cost, or weighted-hyperplane formulation cannot be ruled out by indexed literature searches alone. Independent scientific verification is not claimed.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, first public 2023-04-25, https://arxiv.org/abs/2304.13183.
2. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278v1, 2018, https://arxiv.org/abs/1810.11278.
3. M. I. Ostrovska and M. I. Ostrovskii, *On relations between transportation cost spaces and \(\ell_1\)*, arXiv:1910.03625, 2019, https://arxiv.org/abs/1910.03625.
4. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778, 2018, https://arxiv.org/abs/1809.04778.
5. *Exact numerical index along the short-edge four-cycle deformation*, publicly available mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-numerical-index-along-the-short-edge-four-cycle-deformatio--961105f89184.
6. *Numerical-index-one rigidity for weighted cycles and positive cube sections*, publicly available mathematical result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-numerical-index-one-rigidity-for-weighted-cycles-and-positive-cu--aa457cec74ea.
