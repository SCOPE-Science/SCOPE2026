# Exact endpoint norms and alternating-mask rigidity on regular \(q\)-ary filtrations

## Finding
Fix integers \(q\ge3\) and \(n\ge1\). On the uniform space \(\Omega=\{0,\ldots,q-1\}^n\), let \(E_k\) be conditional expectation onto the first \(k\) coordinates (\(E_0\) is global averaging), and for \(b\in\{0,1\}^n\) let
\[
P_b=\sum_{k=0}^{n-1}b_k(E_{k+1}-E_k).
\]
Set \(\lambda=1/q\), \(c=1-\lambda\), and \(C_{q,n}=\max_b\|P_b\|_{L^\infty\to L^\infty}\). Then the \(L^1\) and \(L^\infty\) operator norms agree for every mask, and the following are **exact**:

For \(n=2m+1\), \(m\ge0\),
\[
C_{q,2m+1}=2c\left[m+1-c\sum_{j=1}^m(m+1-j)\lambda^{2j-1}\right]. \tag{1}
\]
For \(n=2m\), \(m\ge1\),
\[
C_{q,2m}=2c\left[m+1-c\left(\sum_{j=1}^{m-1}(m-j)\lambda^{2j-1}+\sum_{j=0}^{m-1}\lambda^{2j}\right)\right]. \tag{2}
\]
At odd depth, the unique maximizing mask is \((1,0,1,\ldots,0,1)\). At depth two, the unique maximizer is \((1,1)\). At every even depth \(n\ge4\), exactly two masks maximize: \((1,0,1,0,\ldots,1,1)\) and \((1,1,0,1,\ldots,0,1)\); the dots mean alternating intermediate bits, and both endpoint bits are one. In particular,
\[
\lim_{n\to\infty}\frac{C_{q,n}}n=\frac{q-1}{q+1}. \tag{3}
\]
A sharper structural statement holds for every remaining depth at least two: if \(r\in[0,1]\) is the initial state in the Bellman problem defined in the proof, the optimal first action is one when \(r<\lambda\) for even remaining depth and when \(r<c\) for odd remaining depth; at equality, both first actions are optimal. At depth one the first action is one for every \(r<1\). For \(q\ge3\), the odd-depth maximizing mask is rigid, unlike the previously known binary exception.

## Assumptions and scope
All functions are real-valued, the probability measure on \(\Omega\) is uniform, every level of the filtration has the same branching number \(q\), and masks act on *whole martingale-difference levels*, not individual nodes. Every \(P_b\) is the \(L^2\)-orthogonal projection onto the direct sum of the selected martingale-difference spaces. The theorem claims no bound for node-dependent masks, nonuniform branching, infinite depth, or intermediate \(L^p\) exponents. For any fixed mask, sign-valued test functions attain its sharp \(L^\infty\) norm.

## Proof
**Kernel-to-variation identity.** Write \(\ell(x,y)\) for the number of initial matching coordinates. Relative to uniform probability, the kernel of \(E_k\) is \(q^k\mathbf1_{\{\ell(x,y)\ge k\}}\). Consequently, when the first disagreement is at coordinate \(j\), the kernel of \(P_b\) is
\[
K_b(x,y)=(q-1)\sum_{k=0}^{j-2}b_kq^k-b_{j-1}q^{j-1},
\]
whereas on the diagonal \(K_b(x,x)=(q-1)\sum_{k=0}^{n-1}b_kq^k\). The respective proportions in a row are \((q-1)/q^j\) and \(q^{-n}\). Introduce \(r_0=0\) and
\[
r_{k+1}=\lambda r_k+c b_k\qquad(0\le k<n). \tag{4}
\]
Summing absolute kernel values over the mismatch classes gives exactly
\[
\|P_b\|_{\infty\to\infty}=r_n+\sum_{k=0}^{n-1}|r_{k+1}-r_k|. \tag{5}
\]
This value is independent of the evaluation row. The kernel matrix is symmetric, so its maximum absolute column and row sums coincide, establishing the \(L^1\) statement. Choosing the signs of a maximizing kernel row supplies an attaining input.

**Bellman lemma and its proof.** For arbitrary \(r\in[0,1]\), let \(V_t(r)\) be the maximum of the right side of (5) over \(t\) future bits, starting at \(r_0=r\). With \(V_0(r)=r\), the exact recurrence is
\[
V_t(r)=\max\{cr+V_{t-1}(\lambda r),\ c(1-r)+V_{t-1}(\lambda r+c)\}. \tag{6}
\]
Indeed, (4) moves to \(\lambda r\) after bit zero and to \(\lambda r+c\) after bit one; the immediate variations are \(cr\) and \(c(1-r)\), respectively. For \(t=1\), the second action wins for \(r<1\), giving \(V_1(r)=2c+(2\lambda-1)r\).

For every \(t\ge2\), \(V_t\) is the maximum of two affine functions meeting at the **single** threshold
\[
\theta_t=\begin{cases}\lambda,&t\text{ even},\\c,&t\text{ odd}.\end{cases} \tag{7}
\]
The smaller-\(r\) branch chooses bit one, the larger-\(r\) branch chooses bit zero. Here is an algebraic induction, including the threshold verification. Denote the lower-\(r\) branch by \(A_t+\alpha_t r\), the upper-\(r\) branch by \(B_t+\beta_t r\), and write \(\delta_t=\beta_t-\alpha_t\). Set \(\alpha_1=\beta_1=2\lambda-1\), \(\delta_1=0\), and take \(\theta_1=c\) merely as a bookkeeping convention. Since \(\lambda\le c\), the state \(\lambda r\) always lies on the lower branch of \(V_{t-1}\), and \(\lambda r+c\) always lies on the upper branch (at an endpoint equality is harmless). Thus (6) yields
\[
\alpha_t=-c+\lambda\beta_{t-1},\qquad
\beta_t=c+\lambda\alpha_{t-1},\qquad
\delta_t=2c-\lambda\delta_{t-1}. \tag{8}
\]
In particular,
\[
\delta_t=\frac{2c(1-(-\lambda)^{t-1})}{1+\lambda}>0\qquad(t\ge2). \tag{9}
\]
At \(r=0\), the bit-one affine candidate has intercept \(c+B_{t-1}+c\beta_{t-1}\), whereas the bit-zero candidate has intercept \(A_{t-1}\). Their crossing is therefore at
\[
\frac{c(1+\beta_{t-1})-\delta_{t-1}\theta_{t-1}}{\delta_t}. \tag{10}
\]
The claimed alternating values in (7) follow directly from (8)-(9): for even \(t\), \(\beta_t=(c+2\lambda^{t+1})/(1+\lambda)\); for odd \(t\), \(1+\alpha_t=2\lambda(1+\lambda^t)/(1+\lambda)\). Substitution in (10), using \(\theta_1=c\), gives \(\lambda\) for even \(t\) and \(c\) for odd \(t\). For completeness, the only two simplifications are
\[
 c(1+\beta_{2m})-\lambda\delta_{2m}=c\delta_{2m+1},\qquad
 c(1+\alpha_{2m+1})=\lambda\delta_{2m+2}.
\]
The base \(t=2\) has crossing \(\lambda\). This proves (7) and the strict first-action rule away from its threshold.

**Equality masks.** Start (6) at \(r=0\). The first action is uniquely one. After that the state is \(c\). At odd total depth at least three, the remaining depth is even, with threshold \(\lambda<c\), so the next action is uniquely zero; it is then followed by alternating unique actions. At even total depth at least four, the remaining depth is odd and its state is exactly its threshold \(c\); both next actions are optimal. After either choice the state lies strictly away from the threshold for each subsequent stage because \(0<\lambda<c<1\). Exactly the two masks in the finding result. At depth two only \((1,1)\) maximizes. The strict inequality \(c>\lambda\) is essential; at \(q=2\) the odd-depth equality classification changes.

**Closed forms and growth.** Writing (5) as a quadratic function of the bits yields
\[
 r_n+\sum_k|r_{k+1}-r_k|=2c\left(\sum_{k=0}^{n-1}b_k-c\sum_{0\le i<j<n}\lambda^{j-i-1}b_i b_j\right). \tag{11}
\]
For the unique odd-depth mask, the selected positions are \(0,2,\ldots,2m\), and the pair gaps give the geometric sum (1). For an even-depth maximizing mask, the selected positions are \(0,2,\ldots,2m-2,2m-1\), giving (2); reversing the selected positions yields the second mask with the same value. The leading term of the sums in (1)-(2), divided by \(n\), is \(\lambda/(2(1-\lambda^2))\). Applying (11) gives (3).

## Verification
`check.py` checks the exact kernel/variation identity for every whole-level mask through ten levels for each \(3\le q\le7\), enumerates **all** maximizers there, verifies (1)-(2), reconstructs projection matrix rows independently in smaller models, and tests the Bellman envelope at exact rational initial states. It outputs a deterministic assertion count. These finite tests do not prove the theorem at arbitrary depth; the algebraic induction above does.

## Relationship to prior work
Osękowski (2013) proves restricted weak-type estimates for Haar projections and much more general martingale transforms, whereas (1)-(3) give finite-depth *strong endpoint* norms and equality masks for a fixed homogeneous \(q\)-ary filtration. Semenov and Uksusov (2012) and Wark (2015) examine multiplier norms for the classical dyadic Haar basis; their available abstracts concern dyadic multiplier spaces rather than the regular-branching \(q\ge3\) extremal-mask classification. The exact binary whole-level-mask optimization at \(q=2\) is pre-existing and is not included in the novelty assertion. No claim is made that a multiplier representation or kernel row-sum identity is new in itself; the contribution is the optimal all-depth \(q\)-ary branch selection, equality rigidity, and slope (3).

## Limitations
The complete texts of the Semenov–Uksusov 2012 and Wark 2015 papers were not accessible during comparison, leaving a nonzero historical-priority risk under alternative terminology. The online Osękowski full-text HTML was inspected, though some equation displays were not recoverable in the textual rendering. Equations (1)-(3) do not address arbitrary node-dependent Haar multipliers, irregular trees, or infinite-dimensional endpoint boundedness. Only a self-review has been completed; there is no independent audit or certification.

## References
- A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces (2013), DOI: 10.1155/2013/646012, first published 2013-12-05, https://onlinelibrary.wiley.com/doi/10.1155/2013/646012.
- E. M. Semenov and S. N. Uksusov, *Multipliers of the Haar series*, Siberian Mathematical Journal 53 (2012), 310–315, DOI: 10.1134/S0037446612020139, https://www.mathnet.ru/eng/smj2313.
- H. M. Wark, *A remark on the multipliers of the Haar basis of \(L^1[0,1]\)*, Studia Mathematica 227 (2015), 141–148, DOI: 10.4064/sm227-2-4, https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/227/2/91217.
