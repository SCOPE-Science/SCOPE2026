# Two-switch optimality for biased binary two-mer minimizers at the first exceptional window

## Finding
Let \(X_i\) be independent Bernoulli symbols with \(\Pr(X_i=1)=p\), \(0<p<1\). Fix the two-mer length \(k=2\) and choose the leftmost minimum under a strict priority order in every window of \(w\) consecutive two-mers. Write \(d_{w,\pi}(p)\) for the limiting expected proportion of selected two-mer positions under priority order \(\pi\), and let \(d_w^*(p)=\min_\pi d_{w,\pi}(p)\). The following is the exact optimal-order phase diagram for \(2\le w\le9\).

Put \(A=(01,00,10,11)\) and \(A'=(01,00,11,10)\), with priorities written from smallest to largest, and \(B=(11,01,00,10)\). For \(0<p<1/2\) and every \(2\le w\le8\), the orders \(A,A'\) attain \(d_w^*(p)\); these are the only optimal orders for \(3\le w\le8\), while four orders are optimal for \(w=2\).

For \(w=9\), let \(\alpha<\beta\) be the two roots in \((0,1/2)\) of
\[
H(p)=p^8-5p^7+15p^6-16p^5+9p^4-5p^3+13p^2-7p+1.
\]
They are simple, with \(\alpha\in(257/1000,258/1000)\), \(\beta\in(346/1000,347/1000)\), and numerical approximations \(\alpha\approx0.257061407631624\), \(\beta\approx0.346193374721944\). On \((0,\alpha)\cup(\beta,1/2)\), precisely \(A,A'\) are optimal. On \((\alpha,\beta)\), precisely \(B\) is optimal. At each of \(p=\alpha,\beta\), precisely \(A,A',B\) are optimal. At \(p=1/2\), exactly eight strict orders minimize the density, which equals \(263/1024\). For \(1/2<p<1\), complementing every binary symbol in an optimal order for \(1-p\) yields exactly the optimal orders.

In particular, \(w=9\) is the first window width at which any nontrivial open interval of rare-symbol biases changes the optimal binary two-mer ordering.

## Assumptions and scope
The source is an infinite stationary independent binary stream, with independent bits of equal success probability \(p\). The minimizer processes the four labeled two-mers \(00,01,10,11\) under one global strict total order, and equal-priority repeated two-mers are resolved in favor of the leftmost position. A window contains \(w\) two-mer starts and therefore \(w+1\) underlying symbols. Density means the almost-sure limiting selected-start fraction, equivalently its stationary expectation; finite sequence endpoints contribute vanishing boundary terms. No adaptive ranking or string-dependent tie-breaking is allowed.

## Proof
**1. Stationary charged-window identity.** Consider adjacent windows of two-mer starts at positions \(0,\ldots,w-1\) and \(1,\ldots,w\). Their minimizer positions are nondecreasing, because the old minimum either remains, exits at the left, or is displaced by the new rightmost two-mer. Hence the density is exactly the probability that the two chosen positions differ. Only the \(m=w+2\) underlying bits at positions \(0,\ldots,w+1\) matter. For a strict order \(\pi\), let \(c_{\pi,r}\) be the number of length-\(m\) bit words with precisely \(r\) ones for which those two minimizers differ. Independence gives the **exact** polynomial
\[
d_{w,\pi}(p)=\sum_{r=0}^{m}c_{\pi,r}\,p^r(1-p)^{m-r}.
\]
This statement is an identity for the infinite stationary density, not a finite-window approximation.

**2. An integer certificate for global order comparisons.** For \(A\) as above, put \(u=p/(1-2p)\), which bijects \(0<p<1/2\) with \(u>0\). For each order \(\pi\), define
\[
Q_{w,\pi}(u)=(1+2u)^m\bigl(d_{w,\pi}(u/(1+2u))-d_{w,A}(u/(1+2u))\bigr).
\]
Its coefficients are integers:
\[
[u^j]Q_{w,\pi}(u)=\sum_{r=0}^{j}\bigl(c_{\pi,r}-c_{A,r}\bigr)\binom{m-r}{j-r},\qquad0\le j\le m.
\]
The complete finite certificate consists of enumerating the \(24\) strict orders and every one of the \(2^m\) binary contexts, computing these coefficients, and checking their signs. The accompanying exact-integer `verify_exact.py` carries out these quantified loops without external dependencies: for every width \(2\le w\le8\), every coefficient of every \(Q_{w,\pi}\) is nonnegative. The zero polynomials correspond to exactly four orders at \(w=2\) and exactly \(A,A'\) at each \(3\le w\le8\). Since a nonzero polynomial with all nonnegative coefficients is strictly positive at every \(u>0\), this proves those global optima and their complete equality cases.

At \(w=9\), all coefficients of \(Q_{9,\pi}\) are likewise nonnegative for every order except \(B=(11,01,00,10)\) and \(C=(11,01,10,00)\). The second exceptional order is always dominated by \(B\), since exact integer expansion gives
\[
d_{9,C}(p)-d_{9,B}(p)=p(1-p)^{10}>0\qquad(0<p<1).
\]
For all remaining orders, the same nonnegative-coefficient and zero-case check excludes any order other than \(A,A'\) from matching the smaller of \(d_{9,A}\) and \(d_{9,B}\). The resulting global optimum is therefore the smaller of these two explicit density polynomials.

**3. Exact crossing polynomial and two-root proof.** The integer event-count vectors, indexed by number of ones \(r=0,\ldots,11\), are
\[
(c_{A,r})_{r=0}^{11}=(1,2,10,37,85,127,127,85,37,11,3,1)
\]
and
\[
(c_{B,r})_{r=0}^{11}=(1,2,11,38,77,109,131,126,84,36,9,1).
\]
Direct expansion yields
\[
d_{9,A}(p)-d_{9,B}(p)=p^2(p-1)H(p).
\]
To count the roots of \(H\) on \((0,1/2)\), use the same substitution \(p=u/(1+2u)\):
\[
(1+2u)^8H\!\left(\frac{u}{1+2u}\right)
=1+9u+27u^2+11u^3-101u^4-192u^5-57u^6+135u^7+99u^8.
\]
The coefficient signs have precisely two changes, so Descartes' rule of signs bounds the number of positive roots, counted with multiplicity, by two. The exact rational signs of \(H\) at \(257/1000,258/1000\) are respectively positive and negative, and those at \(346/1000,347/1000\) negative and positive. The intermediate value theorem produces two distinct positive roots; Descartes proves there are exactly two and each is simple. The sign of \(p^2(p-1)\) is negative on \((0,1)\), giving the stated order switches.

**4. Symmetry and unbiased point.** Complementing every bit maps a Bernoulli-\(p\) input to Bernoulli-\((1-p)\), preserves the selected-start process, and maps the priority labels \(00\leftrightarrow11\), \(01\leftrightarrow10\). Hence the half-interval classification determines the other half. Finally, direct exact summation of the \(24\) charged-word vectors at \(p=1/2\) gives the unique optimum density value \(526/2048=263/1024\), attained by exactly eight orders when \(w=9\).

## Verification
Run `python3 verify_exact.py` and `python3 verify_independent.py` in a directory containing those two provided, standalone scripts. The first exhaustively evaluates every strict order for widths \(2\) through \(9\), constructs the integer coefficient certificates, checks every asserted equality and inequality, checks the crossing-polynomial identity, verifies Descartes' sign changes and exact rational isolating signs, and verifies complement symmetry and the unbiased count. The second independently enumerates all binary contexts via a different criterion: a newly charged location occurs exactly when the old minimum exits at the left boundary or the entering rightmost two-mer has strictly better priority. It evaluates all \(24\) orders at five exact rational source biases for each width, confirming the first verifier's global minima and the two explicit event vectors. Both scripts finished successfully with terminal success messages. No numerical optimizer or inaccessible external table is needed.

## Relationship to prior work
Chikhi and collaborators introduced frequency-based minimizer ordering in the 2014 de Bruijn-graph representation work (arXiv:1401.5383v1), which motivates optimizing priorities for nonuniform symbol statistics, but does not give the present exact Bernoulli optimality switches. Marçais, DeBlasio, and Kingsford developed asymptotically optimal minimizer schemes (2018), and Shur's 2025 study analyzes all widths, including binary two-mers, under its **uniform** random-string density objective. Those results do not determine the weighted Bernoulli-\(p\) optimum or its switching roots. The exact uniform-density value at \(p=1/2\) is included as verification, **not** claimed as new. Zheng's 2022 dissertation treats minimizer densities and charged contexts extensively, but explicitly uses a uniform distribution in the relevant expectation calculation. Practical adaptive frequency orders and dataset-specific sketch work use different objectives and do not establish this exact global phase diagram.

## Limitations
The classification is restricted to **binary, two-mer, fixed strict total orders and window sizes at most nine**, with iid Bernoulli input; no conclusion is claimed for longer k-mers, general Markov sources, adaptive schemes, or window widths beyond nine. The theorem is mathematically exhaustive for its stated finite order and context sets, not an asymptotic claim about parameter growth or a practical speedup guarantee. The gain at some biases is numerically small (for example, at \(p=3/10\), ordering \(B\) improves density by \(0.00132759207\) over \(A\)). Historical or nonindexed unpublished computations could contain equivalent weighted profiles despite the described source comparisons; no independent external audit has been performed.

## References
1. R. Chikhi, A. Limasset, S. Jackman, J. Simpson, P. Medvedev, *On the representation of de Bruijn graphs*, arXiv:1401.5383v1 (first public 2014-01-21), https://arxiv.org/abs/1401.5383 .
2. G. Marçais, D. DeBlasio, C. Kingsford, *Asymptotically optimal minimizers schemes*, Bioinformatics 34 (2018), https://doi.org/10.1093/bioinformatics/bty258 .
3. H. Zheng, *Theory and Practice of Low-Density Minimizer Sketches*, PhD dissertation (2022), https://kingsfordlab.cbd.cmu.edu/pdf/2022-news-zhengphd.pdf .
4. A. Shur, *On Minimizers of Minimum Density*, arXiv:2506.05277v1 (2025), https://arxiv.org/abs/2506.05277 .
5. D. Flomin, D. Pellow, R. Shamir, *Data Set-Adaptive Minimizer Order Reduces Memory Usage in k-Mer Counting*, J. Comput. Biol. 29 (2022), https://doi.org/10.1089/cmb.2021.0599 .
