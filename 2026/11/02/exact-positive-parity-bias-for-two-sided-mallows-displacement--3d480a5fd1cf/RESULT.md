# Exact positive parity bias for two-sided Mallows displacement

## Finding
For every real \(Q>1\), put \(t=Q^{-1}\in(0,1)\) and let \(\Sigma\) have the stationary two-sided Mallows distribution on permutations of \(\mathbb Z\), with parameter \(t\). Then
\[
\mathbb P(\Sigma(0)\text{ even})-\mathbb P(\Sigma(0)\text{ odd})
=\left(\frac{(t;t)_\infty}{(-t;t)_\infty}\right)^2
=\prod_{k=1}^{\infty}\left(\frac{1-t^k}{1+t^k}\right)^2>0.
\]
Here the \(q\)-shifted factorials are defined below. In the notation of He, Müller and Verstraaten for the limiting expected number of one-cycles in Mallows permutations with \(Q>1\), their Theorem 1.6 identifies \(c_o(Q)=\mathbb P(\Sigma(0)\text{ even})\) and \(c_e(Q)=\mathbb P(\Sigma(0)\text{ odd})\). Thus their proposed strict inequality holds for every \(Q>1\):
\[
c_o(Q)=\frac{1+\Delta(Q^{-1})}{2}>\frac12>
\frac{1-\Delta(Q^{-1})}{2}=c_e(Q),\qquad
\Delta(t)=\prod_{k=1}^{\infty}\left(\frac{1-t^k}{1+t^k}\right)^2.
\]
Moreover, \(c_o(Q)\) is strictly increasing and \(c_e(Q)\) strictly decreasing in \(Q>1\). Their limits as \(Q\downarrow1\) are \(1/2\) and as \(Q\to\infty\) are, respectively, \(1\) and \(0\). In particular, this settles both the strict-inequality and monotonicity questions for these two constants posed in Section 10 of He, Müller and Verstraaten.

## Assumptions and scope
For a finite permutation \(\pi\), Mallows probability at inverse-temperature parameter \(Q\) is proportional to \(Q^{\operatorname{inv}(\pi)}\). The stationary two-sided extension used here instead has parameter \(t=Q^{-1}\in(0,1)\); reversing this parameter is essential. Let \(D=\Sigma(0)\). Define nonnegative right and left inversion counts at zero by
\[
R=\#\{j>0:\Sigma(j)<\Sigma(0)\},\qquad
L=\#\{i<0:\Sigma(i)>\Sigma(0)\}.
\]
These are almost surely finite and satisfy \(D=R-L\) in the balanced two-sided extension. For an integer \(m\ge0\), define \((a;t)_m=\prod_{j=0}^{m-1}(1-at^j)\), with the empty product equal to one; define \((a;t)_\infty\) by its convergent infinite product. In particular,
\[
(t;t)_\infty=\prod_{k=1}^{\infty}(1-t^k),\qquad
(-t;t)_\infty=\prod_{k=1}^{\infty}(1+t^k).
\]
All asserted identities and inequalities hold for every fixed \(0<t<1\), without a limiting interchange in the permutation size.

## Proof
Gnedin and Olshanski's displacement theorem and its conditional generating-function computation (Theorem 5.1 and its proof, especially equations (20)–(23)) give
\[
\mathbb P(R=r)=(1-t)t^r,\qquad
\mathbb E[z^L\mid R=r]=
\prod_{k=r+1}^{\infty}\frac{1-t^k}{1-zt^k}
\quad(r=0,1,2,\ldots;\ |z|\le1).
\]
Since \(D=R-L\) and parity ignores the sign of an integer,
\[
\Delta(t)=\mathbb E[(-1)^D]
=(1-t)\sum_{r=0}^{\infty}(-t)^r
\prod_{k=r+1}^{\infty}\frac{1-t^k}{1+t^k}.
\]
All terms are bounded in absolute value by the geometric weights \((1-t)t^r\), so the series converges absolutely. Using the definitions of the infinite products, the conditional product equals
\[
\prod_{k=r+1}^{\infty}\frac{1-t^k}{1+t^k}
=\frac{(t;t)_\infty}{(-t;t)_\infty}
\frac{(-t;t)_r}{(t;t)_r}.
\]
Consequently,
\[
\Delta(t)=(1-t)\frac{(t;t)_\infty}{(-t;t)_\infty}
\sum_{r=0}^{\infty}\frac{(-t;t)_r}{(t;t)_r}(-t)^r.
\]
The classical \(q\)-binomial identity, valid whenever \(0<t<1\) and \(|z|<1\), is
\[
\sum_{r=0}^{\infty}\frac{(a;t)_r}{(t;t)_r}z^r
=\frac{(az;t)_\infty}{(z;t)_\infty}.
\]
Apply it with \(a=-t\) and \(z=-t\): the series is \((t^2;t)_\infty/(-t;t)_\infty\). Since \((1-t)(t^2;t)_\infty=(t;t)_\infty\), substitution yields
\[
\Delta(t)=\frac{(t;t)_\infty^2}{(-t;t)_\infty^2},
\]
as claimed. The probability identities for \(c_o\) and \(c_e\) then follow from their published identification, together with \(c_o+c_e=1\).

For positivity and strict monotonicity, each \((1-t^k)/(1+t^k)\) lies strictly between zero and one and strictly decreases with \(t\in(0,1)\). The product is positive because the logarithms have absolutely summable magnitudes (for fixed \(t<1\), their tails are \(O(t^k)\)). If \(0<t_1<t_2<1\), comparison of all factors, with a strict inequality already at \(k=1\), gives \(\Delta(t_1)>\Delta(t_2)>0\). Thus \(c_o(Q)\) increases strictly and \(c_e(Q)\) decreases strictly with \(Q=1/t\). As \(t\downarrow0\), absolute summability and dominated convergence in the logarithmic series give \(\Delta(t)\to1\). Finally, \(0<\Delta(t)\le[(1-t)/(1+t)]^2\to0\) as \(t\uparrow1\). This proves every stated endpoint limit.

## Verification
Run `python3 verify_mallows_parity.py` with Python 3 and the standard library; no external packages are required. The program independently compares the first 19 formal power-series coefficients of the signed double series obtained from Gnedin–Olshanski's exact joint inversion-count formula with the proposed product, using integer arithmetic. It then compares six numerical evaluations of an independently summed conditional law to the infinite product and verifies strict ordering on seven parameter values. A successful run prints `CHECKS_PASSED`.

The exact coefficient checks and finite numerical evaluations are corroboration, not a proof for all real \(t\). The general conclusion follows from the probability-generating-function identity, absolute convergence, the \(q\)-binomial theorem, and the monotonic product argument above.

## Relationship to prior work
Gnedin and Olshanski (2011 preprint; 2012 publication), Theorem 5.1, already determined the distribution of the two-sided Mallows displacement and provided the conditional probability-generating function used here; neither ingredient is claimed as new. He, Müller and Verstraaten (first public preprint January 27, 2022; published 2023), Theorem 1.6, identified the two limiting fixed-point constants with displacement parity probabilities and established their limiting endpoint behavior. Their Section 10 explicitly asked for a proof of the strict inequality and strict monotonicity. The present claim is the single closed product and its consequences obtained by evaluating their existing probability representation with a specialized \(q\)-binomial substitution. An earlier equivalent evaluation elsewhere is possible; the scientific conclusion is not claimed as independently audited or historically exhaustive.

The related earlier preprint by Jimmy He (arXiv:2112.09789, first posted December 17, 2021) established broader cycle-limit context and was subsequently merged into arXiv:2201.11610; it is not a source for the product formula asserted here. The elementary \(q\)-binomial theorem is classical (see the NIST Digital Library of Mathematical Functions).

## Limitations
The result concerns the stationary balanced two-sided Mallows process at each fixed \(t\in(0,1)\), and the associated limiting fixed-point constants for fixed \(Q>1\). It gives no rate of convergence in finite permutation size and no assertion about a joint regime where \(Q\) depends on that size or equals exactly one. It does not resolve analogous questions for higher cycle counts. Numerical checking does not establish absolute historical novelty; priority remains subject to further literature review. Independent mathematical audit has not been performed.

## References
1. A. Gnedin and G. Olshanski, *The two-sided infinite extension of the Mallows model for random permutations*, arXiv:1103.1498 (first public March 8, 2011), *Advances in Applied Mathematics* **48** (2012), Theorem 5.1, equations (20)–(23). https://arxiv.org/abs/1103.1498
2. J. He, T. Müller and T. W. Verstraaten, *Cycles in Mallows random permutations*, arXiv:2201.11610 (first public January 27, 2022), *Random Structures & Algorithms* **63** (2023), Theorem 1.6 and Section 10. https://arxiv.org/abs/2201.11610 ; https://doi.org/10.1002/rsa.21169
3. J. He, *A central limit theorem for cycles of Mallows permutations*, arXiv:2112.09789 (first public December 17, 2021; merged into the preceding paper). https://arxiv.org/abs/2112.09789
4. NIST Digital Library of Mathematical Functions, Section 17.5, \(q\)-binomial series identity. https://dlmf.nist.gov/17.5
