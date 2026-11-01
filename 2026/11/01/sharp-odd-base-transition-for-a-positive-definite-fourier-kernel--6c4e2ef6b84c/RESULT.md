# Sharp odd-base transition for a positive-definite Fourier kernel on the circle

## Finding
Let \(E_k\) be the elementary symmetric polynomial of degree \(k\) in seven variables, with \(E_0=1\), and define
\[
P(y_1,\ldots,y_7)=\frac{21+4E_2(y)+4E_3(y)+E_4(y)}{280}.
\]
For each odd integer \(q\ge3\), define the real trigonometric polynomial on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\)
\[
F_q(t)=P(\cos t,\cos(qt),\ldots,\cos(q^6t)),
\]
and eight circle points \(t_0=0\) and
\[
t_j=\frac{\pi(q-1)}{q^j}\pmod{2\pi},\qquad 1\le j\le7.
\]
Write \(K_q=[F_q(t_j-t_k)]_{0\le j,k\le7}\) and \(J_8\) for the all-ones matrix. Every \(F_q\) is continuous, real-valued, nonnegative, positive definite, and satisfies \(F_q(0)=1\). The following is a **complete sharp odd-base dichotomy for this specified family and these specified nodes**:
\[
\boxed{K_q-\tfrac18J_8\succ0\quad\Longleftrightarrow\quad q\in\{3,5,7,9,11,13,15,17,19,21,23\},}
\]
where the quantifier on \(q\) is over all odd integers \(q\ge3\). For every odd \(q\ge25\), the same fixed vector \(c=(-1,1,1,1,1,1,1,1)^T\) satisfies
\[
\boxed{c^T(K_q-\tfrac18J_8)c<0.}
\]
Thus \(25\) is the **first odd lacunarity ratio** in this canonical compression at which the kernel matrix violates the proposed universal lower bound. In particular, the bound fails already for a nonnegative positive-definite trigonometric polynomial on the one-dimensional torus. Furthermore, the **strictly positive** normalized kernel \(\widetilde F_q=(99999F_q+1)/100000\) has the same strict-satisfaction/violation dichotomy at the same eight nodes. The contribution is the exact all-odd-base classification, not the mere existence of a circle counterexample (which follows more generally from a previously known multidimensional witness).

## Assumptions and scope
Positive definiteness means that \([F(x_j-x_k)]\) is positive semidefinite for any finite set of circle points; \(\succ0\) denotes strict positive definiteness of the stated finite matrix. Only odd integer bases \(q\ge3\), the explicit seven-frequency tower, the fixed polynomial \(P\), and the specified eight nodes are asserted. The question is whether \(K_q\succeq J_8/8\), not whether \(K_q\) itself is positive semidefinite (the latter always holds).

## Proof
**1. The kernel hypotheses.** The polynomial \(P\) is affine in every coordinate. Its value at a cube vertex with \(r\) negative coordinates is
\[
P(\varepsilon)=\frac{(r-2)(r-3)(r-7)(r-10)}{420}\ge0,\qquad r=0,1,\ldots,7.
\]
The vertex values in increasing order of \(r\) are \(1,9/35,0,0,3/35,1/7,4/35,0\). Multiaffine interpolation therefore gives \(P\ge0\) on \([-1,1]^7\). Every product of cosine factors is a nonnegative linear combination of characters, and the four coefficients in the displayed definition of \(P\) are nonnegative. Hence \(F_q\) has nonnegative Fourier coefficients and is positive definite. The binomial identity \(21+4\binom72+4\binom73+\binom74=280\) gives \(F_q(0)=1\).

**2. The limiting obstruction.** Fix \(j\in\{1,\ldots,7\}\) and write \(v_j\in\{-1,1\}^7\) for the vertex with a negative coordinate precisely at position \(j\); let \(v_0=(1,\ldots,1)\). As odd \(q\to\infty\), the seven-dimensional cosine vector at \(t_j\) tends to \(v_j\), and at \(t_j-t_k\) for positive distinct \(j,k\) it tends to the vertex with two negative coordinates. Accordingly, \(K_q\) tends entrywise to
\[
K_\infty=\begin{pmatrix}1&(9/35)\mathbf1_7^T\\(9/35)\mathbf1_7&I_7\end{pmatrix}.
\]
For \(c=(-1,1,\ldots,1)^T\), \(\sum_jc_j=6\), so direct multiplication yields
\[
\Delta_\infty:=c^T(K_\infty-J_8/8)c=8-14(9/35)-36/8=-1/10.
\]
The limiting matrix and its quadratic gap are those of the multidimensional construction in [2]; their use here is explicit prior input, not new work.

**3. A uniform infinite-tail certificate.** For odd \(q\), all phases \(q^{i-1}t_j/\pi\) with \(i>j\) are even integers. For a positive node index \(j\), the phase at coordinate \(i=j\) differs from an odd integer by \(1/q\), and earlier coordinates have phases of magnitude at most \(1/q\). For a difference \(t_j-t_k\) with \(1\le j<k\le7\), the two exceptional coordinates \(j\) and \(k\) approach the value \(-1\); the phase at coordinate \(j\) is within \(2/q\) of an odd integer, and all remaining nonexact phases are within \(1/q\) of an integer of the appropriate parity. By \(1-\cos u\le u^2/2\), in every case, including \(t_0-t_j\), the seven cosine values are within
\[
\sum_{i=1}^7|\cos(q^{i-1}(t_j-t_k))-(v_{jk})_i|\le\frac{5\pi^2}{q^2}
\]
of the applicable cube vertex \(v_{jk}\). Moreover,
\[
\left|\frac{\partial P}{\partial y_i}\right|
\le\frac{4\binom61+4\binom62+\binom63}{280}=\frac{13}{35}
\]
on the cube. The diagonal terms in \(\Delta_q=c^T(K_q-J_8/8)c\) are exact. There are \(56\) ordered off-diagonal terms, each with coefficient of modulus one. Therefore
\[
|\Delta_q+1/10|\le56\frac{13}{35}\frac{5\pi^2}{q^2}<\frac{1040}{q^2}.
\]
Because \(1040/103^2<1/10\), this proves \(\Delta_q<0\) for **every odd \(q\ge103\)** without computation.

**4. Exact finite bridge and small-base positivity.** The complete, dependency-free `CHECK.py` performs outward-rounded integer interval arithmetic with scale \(10^{35}\). It obtains certified enclosing intervals for \(\pi\) from Machin's arctangent identity and alternating rational series, reduces every cosine argument modulo integral multiples of \(\pi\), and encloses the residual cosine on \([-\pi/2,\pi/2]\) by its degree-\(22\) alternating Taylor polynomial and the nonnegative degree-\(24\) remainder bound. All arithmetic and comparisons thereafter are exact integers.

For each of the eleven odd bases \(3\le q\le23\), the checker encloses all eight **leading principal minors** of \(K_q-J_8/8\) and proves that every one is positive. The smallest certified lower bound over these \(88\) minors is greater than \(0.00021359\). Sylvester's criterion proves strict positive definiteness at each such base. For each of the thirty-nine odd bases \(25\le q\le101\), it certifies \(\Delta_q<0\) directly, with the largest certified upper bound below \(-0.0092531\) (attained for \(q=25\)). These \(39\) bases plus step 3 cover all odd \(q\ge25\), completing the claimed dichotomy. This exhaustive finite reduction is justified by the analytical tail bound, not by extrapolation from the finite checks.

**5. Strict pointwise positivity without changing the threshold.** Put \(\delta=1/100000\), \(\widetilde F_q=(1-\delta)F_q+\delta\), and \(\widetilde M_q=[\widetilde F_q(t_j-t_k)]-J_8/8\). This kernel is normalized, positive definite and satisfies \(\widetilde F_q\ge\delta>0\) everywhere. With \(M_q=K_q-J_8/8\), one has \(\widetilde M_q=(1-\delta)M_q+7\delta J_8/8\), which is positive definite for each odd \(3\le q\le23\). For the fixed witness, \(c^T\widetilde M_qc=(1-\delta)\Delta_q+63\delta/2\). For \(25\le q\le101\), the certified bound \(\Delta_q<-9/1000\) makes this expression negative. For odd \(q\ge103\), the tail bound gives the explicit strict rational inequality
\[
(1-\delta)\left(-\frac1{10}+\frac{1040}{103^2}\right)+\frac{63\delta}{2}=-\frac{4389489}{2652250000}<0.
\]
Therefore the same sharp cutoff persists with uniformly strictly positive function values.

## Verification
Run `python3 CHECK.py` in the directory containing that file. Only the Python standard library is needed. It recomputes all \(88\) positive leading-minor enclosures, all \(39\) strictly negative signed-defect enclosures, the polynomial's cube-vertex values, and the exact rational tail inequality. The checker also verifies the strict-positive perturbation inequalities. The certificate computes rather than hard-codes the signs of the trigonometric determinants. The output is a strict-sign certificate; displayed decimal approximations are informational only.

## Relationship to prior work
Hinrichs and Vybíral [1] formulated the normalized kernel lower-bound conjecture, including its torus version. Vybíral [2] explicitly disproved the Euclidean version in seven dimensions and supplied the polynomial \(P\), the corner matrix \(K_\infty\), and its negative \(-1/10\) witness. This source can be restricted to one-dimensional dense or lacunary directions to obtain *existence* of a circle counterexample. Accordingly **that existence alone is not claimed as original**. The new information is the sharp threshold **among every odd geometric base in the stated explicit compression**, including the rigorous positive-matrix side below \(25\) and a proof of failure for all odd bases from \(25\) onward. Neither [1] nor the inspected complete text of [2] gives this base-dependent phase classification.

## Limitations
The cutoff \(25\) is not a minimum across all possible one-variable trigonometric polynomials, all frequency sets, all node sets, or even all compression schemes of \(P\). It concerns only the fixed family and eight nodes. No assertion is made about even bases or about the pointwise strict positivity of \(F_q\). The result relies on the pre-existing seven-variable witness for its motivating polynomial; potential equivalent coverage in unindexed literature remains an originality risk. The finite signs are proved through a transparent reproducible integer certificate, not an independent external audit.

## References
[1] A. Hinrichs and J. Vybíral, *On positive positive-definite functions and Bochner's theorem*, Journal of Complexity 27 (2011), 264–272, DOI: 10.1016/j.jco.2011.01.002; author-hosted complete text: https://kmlinux.fjfi.cvut.cz/~vybirja2/publ/Vybiral19.pdf.

[2] J. Vybíral, *An explicit counterexample to the Hinrichs--Vybiral conjecture*, first public arXiv submission 2026-09-18, arXiv:2609.21733, https://arxiv.org/abs/2609.21733, Sections 1–4.
