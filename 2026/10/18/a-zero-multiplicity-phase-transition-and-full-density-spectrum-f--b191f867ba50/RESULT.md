# A zero-multiplicity phase transition and full density spectrum for metallic-mean Beatty arrays

## Finding
For every integer \(c\ge2\), put \(\alpha=(c+\sqrt{c^2+4})/2\), \(R_j=\{\lfloor k\alpha^j\rfloor:k\ge1\}\) for \(j\ge1\), and \(a_c(N)=\#\{j\ge1:N\in R_j\}\) for positive integers \(N\). For every integer \(v\ge0\), the natural density
\[
 d_{c,v}=\lim_{X\to\infty}\frac{1}{X}\#\{1\le N\le X:a_c(N)=v\}
\]
exists and is strictly positive. More precisely,
\[
 d_{c,0}\ge 1-\frac1{\alpha-1}>0,\qquad
 d_{c,1}\ge\frac{\alpha-2}{\alpha(\alpha-1)}>0.
\]
For \(v\ge2\), the generalized Lucas number \(L_{4v-5}\) lies in exactly \(v\) rows: in row \(R_{4v-5}\) and in all rows \(R_i\) with \(i\) odd and \(1\le i\le 2v-3\). In addition, an explicit circular neighborhood of its orbit point contains a positive-measure subset realizing precisely \(v\) rows. Thus the full multiplicity spectrum \(\{0,1,2,\ldots\}\) occurs with positive density for each \(c\ge2\), contrasting with the golden-ratio case \(\(c=1\)\), where multiplicity zero never occurs.

## Assumptions and scope
All parameters \(c\) are fixed positive integers at least two. Write \(F_0=0,F_1=1\) and \(L_0=2,L_1=c\), with \(F_{j+2}=cF_{j+1}+F_j\) and \(L_{j+2}=cL_{j+1}+L_j\). The powers \(\alpha^j\) are irrational for \(j\ge1\). Each positive integer lies in only finitely many rows, since \(\min R_j=\lfloor\alpha^j\rfloor\to\infty\). Endpoints of arcs below do not contain orbit points, so no ambiguous endpoint convention affects the integer claim.

## Proof
**1. One-circle coding.** The identities \(\alpha^j=F_j\alpha+F_{j-1}\) and \(\alpha^{-j}\equiv(-1)^{j+1}F_j\alpha\pmod{1}\) follow from the quadratic equation. For any real irrational \(\theta>1\), an integer \(N\ge1\) belongs to \(\{\lfloor k\theta\rfloor:k\ge1\}\) exactly when \(\{N/\theta\}>1-1/\theta\): equivalently \(\lfloor(N+1)/\theta\rfloor-\lfloor N/\theta\rfloor=1\). Define the circle set
\[
 S_j=\{x\in\mathbb R/\mathbb Z:\{(-1)^{j+1}F_jx\}>1-\alpha^{-j}\}.
\]
Then \(N\in R_j\iff x_N:=\{N\alpha\}\in S_j\). Each \(S_j\) is a union of \(F_j\) equal arcs, has measure \(\lambda(S_j)=\alpha^{-j}\), and has period \(1/F_j\). Put \(A(x)=\sum_{j\ge1}{\bf1}_{S_j}(x)\). Since \(\sum_j\lambda(S_j)<\infty\), \(A(x)<\infty\) almost everywhere.

**2. Existence of natural densities.** For fixed \(M\), \(A_M(x)=\sum_{j\le M}{\bf1}_{S_j}(x)\) has finitely many discontinuities. Irrational-rotation equidistribution gives the natural density of \(A_M(x_N)=v\) as \(\lambda\{A_M=v\}\). Moreover, for every \(j\), the number of \(N\le X\) in \(R_j\) is at most \(X\alpha^{-j}+1\), and no row with \(\alpha^j>X+1\) contributes. Thus
\[
 \limsup_{X\to\infty}\frac1X\#\{N\le X:A(x_N)\ne A_M(x_N)\}
 \le\sum_{j>M}\alpha^{-j}.
\]
The measure of \(\{A\ne A_M\}\) satisfies the same bound. Letting \(M\to\infty\) proves both existence of every \(d_{c,v}\) and the formula \(d_{c,v}=\lambda\{A=v\}\).

**3. Zero and one multiplicity.** By the union bound, \(\lambda\{A=0\}\ge1-\sum_{j\ge1}\alpha^{-j}=1-1/(\alpha-1)>0\), since \(\alpha>2\). The set \(S_1\setminus\bigcup_{j\ge2}S_j\) consists of points with multiplicity one, so its measure is at least \(\alpha^{-1}-\sum_{j\ge2}\alpha^{-j}=(\alpha-2)/(\alpha(\alpha-1))>0\).

**4. Explicit integer witnesses for all higher multiplicities.** For odd \(m\ge3\), \(L_m=\alpha^m-\alpha^{-m}\). For \(i=m\), \(\{L_m\alpha^{-m}\}=1-\alpha^{-2m}>1-\alpha^{-m}\). For \(i>m\), \(L_m\alpha^{-i}=\alpha^{m-i}-\alpha^{-m-i}\) lies between zero and \(\alpha^{-1}<1-\alpha^{-i}\); hence those rows are excluded. If \(1\le i<m\) is even, reducing \(\alpha^{m-i}\) modulo one gives \(\{L_m\alpha^{-i}\}=\alpha^{i-m}-\alpha^{-m-i}<\alpha^{-1}<1-\alpha^{-i}\). If \(i<m\) is odd, the fractional part is \(1-\alpha^{i-m}-\alpha^{-m-i}\). The row membership criterion becomes \(\alpha^{2i-m}+\alpha^{-m}<1\), which holds for \(i\le(m-1)/2\) (since \(\alpha^{-1}+\alpha^{-3}<1\)) and fails for \(i\ge(m+1)/2\). Consequently exactly \(1+(m-1)/4\) rows contain \(L_m\) when \(m\equiv3\pmod4\). Taking \(m=4v-5\) gives \(a_c(L_m)=v\) for every \(v\ge2\).

**5. Positive density around each witness.** We establish an explicit neighborhood argument for any \(N=L_m\) as above. The quadratic norm gives the uniform irrationality estimate
\[
 \|q\alpha\|>\frac1{Cq}\quad(q\ge1),\qquad C=\alpha+\alpha^{-1}+\tfrac12,
\]
where \(\|\cdot\|\) denotes distance to the nearest integer. Indeed, for nearest integer \(p\), \((p-q\alpha)(p+q\alpha^{-1})\) is a nonzero integer and the second factor is at most \(Cq\). Put
\[
 R=\lfloor\log_\alpha(N+1)\rfloor+3,\qquad
 \delta=\frac1{2C(N+1)F_R^2},\qquad
 W=\{x:\operatorname{dist}_{\mathbb R/\mathbb Z}(x,x_N)<\delta\}.
\]
For \(i\le R\), every orbit value \(\{N\alpha^{-i}\}\) is separated from both arc endpoints by at least \(1/[C(N+1)F_i]\), because the endpoints correspond to the nearest integers for \(N\alpha^{-i}\) and \((N+1)\alpha^{-i}\). A shift by at most \(\delta\) in \(x\) changes the relevant fractional part by at most \(F_i\delta\), so no membership among the first \(R\) rows changes anywhere on \(W\). In particular, their common count is \(v\).

For \(i>R\), the center fractional part equals \(N\alpha^{-i}\in(0,1-\alpha^{-i})\), and \((2N+1)\alpha^{-i}<1\). Therefore \(W\cap S_i=\varnothing\) whenever \(F_i\delta\le N\alpha^{-i}\). Since \(F_i\alpha^i\) increases strictly, the remaining possibly active indices form a tail starting at an index \(j_0>R\), the first satisfying \(F_{j_0}\delta>N\alpha^{-j_0}\).

An interval of length \(2\delta\) intersects a periodic union of arcs of period \(1/F_i\) and overall density \(\alpha^{-i}\) in measure at most \((2\delta+F_i^{-1})\alpha^{-i}\). The recurrences give \(\alpha^{i-2}\le F_i\le\alpha^{i-1}\) for every \(i\ge1\). Consequently,
\[
 \sum_{i\ge j_0}\lambda(W\cap S_i)
 \le\frac{2\delta\alpha^{-j_0}}{1-\alpha^{-1}}
 +\frac{\alpha^2\alpha^{-2j_0}}{1-\alpha^{-2}}.
\]
The defining inequality for \(j_0\) yields \(\alpha^{-2j_0}<\delta/(N\alpha)\), and \(j_0\ge4\). For \(c\ge2\), we have \(\alpha>2\), \(N\ge L_3=c^3+3c\), \(\alpha\le5c/4\), and \(N\ge7c\). Therefore
\[
 \frac{\alpha}{N(1-\alpha^{-2})}<\tfrac14,
 \qquad \frac{2\alpha^{-4}}{1-\alpha^{-1}}<\tfrac18.
\]
The measure of all undesirable high-row memberships inside \(W\) is thus below \(3\delta/8\), while \(\lambda(W)=2\delta\). On a subset of \(W\) of positive measure, no high row occurs, and hence \(A=v\). This proves \(d_{c,v}>0\) for all \(v\ge2\), completing the proof.

**6. Phase contrast.** For \(\(c=1\)\), \(\alpha=\varphi\) and \(\alpha^2=\alpha+1\). The complementary Beatty theorem gives \(R_1\cup R_2=\mathbb N\); multiplicity zero is therefore impossible. The strict emergence of positive-density uncovered integers at \(c=2\) is the asserted boundary.

## Verification
The accompanying `verify.py` computes \(\lfloor k\alpha^j\rfloor\) with integer square roots (no floating-point approximation), tests every asserted generalized Lucas witness at \(\(c=2,3,4\)\) and \(\(m=3,7,11\)\), and checks exact membership arrays on initial integer ranges. Execute `python3 verify.py`; success prints `VERIFY_OK`. The infinite density assertions follow from the proof rather than from these finite checks.

## Relationship to prior work
Ashburn, *On three conjectures of Kimberling concerning the array \(\lfloor k\varphi^n\rfloor\)* (arXiv:2610.05776, initially publicly posted 2026-10-05), proves positivity of every **positive** occurrence-count density for the golden ratio \(\(c=1\)\) and identifies the corresponding Lucas witness pattern. Its statement does not cover the \(c\ge2\) zero-multiplicity phase or the all-metallic full positive-density spectrum. Noppakaew, Kanwarunyu and Wanitchatchawan, *\(k\)-Fibonacci Numbers and \(k\)-Lucas Numbers in Beatty Sequences Generated by Powers of Metallic Means* (Fibonacci Quarterly 61 (2023), 167–177), establish metallic-mean identities and Lucas–Beatty membership relations, but do not establish multiplicity densities. The generalized Lucas identity alone does not prove positive density: the separation-of-arcs and controlled-tail argument above supplies that missing step. A broader unpublished or implicit extension of Ashburn's argument remains a possible literature overlap.

## Limitations
This theorem addresses **fixed integer** metallic parameters \(c\ge2\) and the unweighted row-occurrence count. It asserts existence and positivity of the density of each fixed multiplicity, not formulas for \(d_{c,v}\) for \(v\ge2\), uniform asymptotics in \(c,v\), or quantitative rates of convergence. The proof is mathematical, not an independent external audit.

## References
1. A. Ashburn, *On three conjectures of Kimberling concerning the array \(\lfloor k\varphi^n\rfloor\)*, arXiv:2610.05776 (2026-10-05), https://arxiv.org/abs/2610.05776.
2. P. Noppakaew, P. Kanwarunyu, P. Wanitchatchawan, *\(k\)-Fibonacci Numbers and \(k\)-Lucas Numbers in Beatty Sequences Generated by Powers of Metallic Means*, Fibonacci Quarterly 61 (2023), 167–177, https://www.fq.math.ca/Papers/61-2/noppakaew10042022.pdf.
3. S. Beatty, *Problem 3173*, American Mathematical Monthly 33 (1926), 159; the complementary Beatty theorem is also attributed to Rayleigh.
