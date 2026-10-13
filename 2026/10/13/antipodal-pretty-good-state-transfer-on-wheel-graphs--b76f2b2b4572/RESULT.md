# Antipodal pretty good state transfer on wheel graphs

## Finding
For each even integer \(n\geq 4\), let \(W_{n+1}=K_1\vee C_n\) be the unweighted wheel graph with a central hub and rim vertices indexed by \(\mathbb Z/n\mathbb Z\). Write \(A\) for its adjacency matrix and \(U(t)=\exp(itA)\). Then pretty good state transfer from rim vertex \(0\) to rim vertex \(n/2\) occurs **if and only if** \(n=2^r\) for an integer \(r\geq 3\). In every such case the transfer is not perfect at any positive time. Consequently no unweighted wheel of even rim order at least four has perfect transfer between antipodal rim vertices.

For each qualifying \(n\), the approximating evolution times can be chosen from the discrete set \(2\pi\mathbb Z_{>0}\), and their transfer phase converges to \(1\).

## Assumptions and scope
All edges have weight one, the graph is simple and finite, and the Hamiltonian is **adjacency**, not the combinatorial or normalized Laplacian. A state has pretty good transfer from \(u\) to \(v\) when a sequence of positive real times \(t_j\) and a fixed complex unit \(\gamma\) satisfy \(\|U(t_j)e_u-\gamma e_v\|\to 0\). Perfect transfer is the same equality at one positive time. We consider only pairs of diametrically opposite *rim* vertices and only even rim orders \(n\geq 4\); nothing is claimed about hub transfer, other vertex pairs, odd rim orders, or weighted variants.

Put \(\zeta=\exp(2\pi i/n)\), \(\theta_k=\zeta^k+\zeta^{-k}=2\cos(2\pi k/n)\) for \(1\leq k<n\), and \(\lambda_\pm=1\pm\sqrt{n+1}\). The exact eigenphase criterion for antipodal pretty good transfer is that some common unit complex number \(\gamma\) and some times \(t_j\) obey
\[
 e^{it_j\lambda_+},e^{it_j\lambda_-}\longrightarrow\gamma,
 \qquad e^{it_j\theta_k}\longrightarrow(-1)^k\gamma\quad(1\leq k<n).
\]

## Proof
**Spectral reduction.** The normalized rim Fourier vectors \(f_k=n^{-1/2}(1,\zeta^k,\ldots,\zeta^{(n-1)k},0)^T\), indexed by \(1\leq k<n\), are adjacency eigenvectors of the wheel with eigenvalues \(\theta_k\), since their rim coordinate sum is zero. The invariant span of the rim-uniform vector \(f_0\) and the hub vector has matrix
\[
 \begin{pmatrix}2&\sqrt n\\\sqrt n&0\end{pmatrix},
\]
whose eigenvalues are precisely \(\lambda_\pm\). The initial rim basis vector has nonzero projections on all \(f_k\) and on both eigenvectors in this two-dimensional block. The target antipode changes the Fourier projections by \((-1)^k\) and leaves the rim-uniform projection unchanged. Orthogonality and finite dimension therefore give the displayed phase criterion, also when eigenvalues coincide. This criterion is both necessary and sufficient.

**Three obstructions.** Every pair \(\lambda_+,\lambda_-\) sums to \(2\). Hence the criterion implies \(e^{2it_j}\to\gamma^2\), while the mode \(k=n/2\), which has eigenvalue \(-2\), implies \(e^{-2it_j}\to(-1)^{n/2}\gamma\).

If \(n\equiv2\pmod4\), the two modes \(k=1\) and \(k=1+n/2\) have opposite eigenvalues and opposite parities. Multiplying their demanded limits gives \(\gamma^2=-1\). But then \(e^{-2it_j}\to-1\), while the \(k=n/2\) condition gives \(e^{-2it_j}\to-\gamma\), forcing \(\gamma=1\), a contradiction.

If \(n\equiv4\pmod8\), the mode \(k=n/4\) has eigenvalue \(0\) and odd index, forcing \(\gamma=-1\). The \(k=n/2\) mode has even index, so \(e^{-2it_j}\to-1\), whereas the two exceptional eigenvalues demand \(e^{2it_j}\to\gamma^2=1\), again impossible.

It remains to rule out orders divisible by \(8\) that have an odd prime factor \(p\). Put \(q=n/p\), which is even and at least \(8\). For either \(k=1\) or \(k=2\), the indices \(k+aq\), with \(0\leq a<p\), lie between \(1\) and \(n-1\), and all have the same parity as \(k\). The elementary root-of-unity identity
\[
 \sum_{a=0}^{p-1}\theta_{k+aq}
 =\zeta^k\sum_{a=0}^{p-1}(\zeta^q)^a
 +\zeta^{-k}\sum_{a=0}^{p-1}(\zeta^{-q})^a=0
\]
forces \(1=[(-1)^k\gamma]^p\) by the phase criterion. The choices \(k=1\) and \(k=2\) give \(1=(-\gamma)^p\) and \(1=\gamma^p\), contradictory for odd \(p\). Thus only powers of two can work, and the preceding cases exclude \(n=4\).

**Sufficiency at powers of two.** Let \(n=2^r\) for \(r\geq4\) and set \(m=n/4\). We first establish the exact rational linear independence of
\[
 1,\theta_1,\ldots,\theta_{m-1},\sqrt{n+1}.
\]
The cyclotomic polynomial is \(\Phi_{2^r}(z)=z^{n/2}+1\), of degree \(n/2\). Multiplying any rational relation among \(1,\theta_1,\ldots,\theta_{m-1}\) by \(\zeta^{m-1}\) produces a polynomial of degree at most \(2m-2<n/2\). Its monomial positions are distinct, so no nontrivial relation exists. The \(m\) numbers consequently form a basis of the real cyclotomic field \(K=\mathbb Q(\zeta+\zeta^{-1})\), which has degree \(m\).

Also, \(\sqrt{n+1}\notin K\): the odd integer \(n+1\) is not a square for \(r\geq4\). Indeed, if \(s^2=2^r+1\), then \((s-1)(s+1)=2^r\) consists of two positive powers of two differing by two, implying \(s=3\) and \(r=3\). The Galois group of \(\mathbb Q(\zeta_{2^r})\) is \(C_2\times C_{2^{r-2}}\): the unit \(5\) has order \(2^{r-2}\) modulo \(2^r\), since \(\nu_2(5^{2^j}-1)=j+2\), and \(-1\) supplies the other generator. Thus there are exactly three quadratic subfields. They are visibly \(\mathbb Q(i)\), \(\mathbb Q(\sqrt2)\), and \(\mathbb Q(\sqrt{-2})\), since the primitive eighth root yields both \(i\) and \(\sqrt2\). The sole real quadratic subfield is \(\mathbb Q(\sqrt2)\), which cannot equal \(\mathbb Q(\sqrt{n+1})\) for odd nonsquare \(n+1\). This proves the asserted independence.

By Kronecker's simultaneous approximation theorem for integer multiples of rationally independent numbers together with \(1\), there exist arbitrarily large positive integers \(j\) such that, simultaneously,
\[
 j\theta_k\longrightarrow\begin{cases}1/2\pmod1,&k\text{ odd},\\0\pmod1,&k\text{ even},\end{cases}
 \quad(1\leq k<m),\qquad j\sqrt{n+1}\longrightarrow0\pmod1.
\]
Take \(t=2\pi j\). The exceptional eigenvalues then have phases \(e^{it\lambda_\pm}\to1\), and \(e^{it\theta_k}\to(-1)^k\) for \(1\leq k<m\). The identities \(\theta_{n/2-k}=-\theta_k\), \(\theta_{n/2+k}=-\theta_k\), \(\theta_{n-k}=\theta_k\), together with even \(n/2\), extend those limits to every mode. The remaining values \(\theta_m=0\) and \(\theta_{n/2}=-2\) already have the correct phases, because \(m\) is even and \(t\in2\pi\mathbb Z\). This is the phase criterion with \(\gamma=1\).

For \(r=3\), one has \(n=8\), \(\sqrt{n+1}=3\), and the nonintegral rim eigenvalues are \(\pm\sqrt2\). Density of the fractional parts of \(j\sqrt2\) gives positive integers \(j\) approaching the phase \(1/2\pmod1\). Again take \(t=2\pi j\). The exceptional eigenvalues \(4,-2\) have phase one, all zero and integer rim eigenvalues have their required phases, and the odd modes \(\pm\sqrt2\) tend to phase minus one. Hence transfer is pretty good.

**No perfect transfer.** For a qualifying \(n=2^r\), \(r\geq3\), the zero rim mode \(k=n/4\) has even index, so any perfect-transfer phase must be \(\gamma=1\). The rim eigenvalue \(-2\) at \(k=n/2\) then forces \(t\in\pi\mathbb Z\). If \(r\geq4\), equality of both exceptional phases with one implies \(e^{2it\sqrt{n+1}}=1\), i.e. \(j\sqrt{n+1}\in\mathbb Z\) when \(t=\pi j\), contradicting irrationality at positive time. At \(r=3\), the odd rim eigenvalue \(\sqrt2\) instead requires \(e^{i\pi j\sqrt2}=-1\), likewise impossible for positive integer \(j\). Since perfect transfer implies pretty good transfer, the previously eliminated rim orders have no perfect transfer either.

## Verification
The standalone script `verify.py` (Python 3 standard library) checks the Fourier and exceptional wheel eigenvectors for every even rim size from \(4\) through \(48\), the cyclotomic monomial-support separation at rim sizes \(2^r\) for \(3\leq r\leq10\), and finite instances of the three phase-obstruction mechanisms. It also uses the exact eigenprojector-weight formula to search for accurate approximate-transfer times at rim sizes \(8\) and \(16\). A completed invocation of `python3 verify.py` returned the `VERIFY_OK` line described in `VERIFICATION.md`. These finite calculations illustrate and cross-check the formulae but are not substitutes for the unrestricted proof above.

## Relationship to prior work
Pal and Bhattacharjya (2017) completely classified pretty good transfer in the cycles \(C_n\) and their complements, and proved cyclotomic independence and the odd-prime obstruction for cycles. Those established facts and the Kronecker method are credited. Their families formed by adding *circulant* edges or taking Cartesian products do not contain the wheel \(K_1\vee C_n\), which has an additional hub and two different vertex degrees. The present proof must also control the independent exceptional frequency \(\sqrt{n+1}\), absent from a cycle.

Coutinho et al. (2022) gave general exact criteria and algorithms for deciding pretty good transfer on integral adjacency Hamiltonians; a general decision criterion is not the stated closed-form all-order classification. Kirkland and Monterde (2023) provided the join eigenvalue formula and classified *perfect* transfer and strong cospectrality in joins. Their general join spectral lemma agrees with the two exceptional eigenvalues here, but their results do not state the pretty-good classification of antipodal wheel vertices. A differently indexed equivalent result elsewhere remains possible.

## Limitations
The theorem is an exact existence/nonexistence classification, not a quantitative upper bound on the waiting time needed to achieve a specified fidelity. It does not address other vertex pairs, imperfect transfer maxima at excluded orders, weighted couplings, perturbations, or other Hamiltonians. Approximate numerical witnesses in the verifier are finite checks only; the infinite sequence is established by Kronecker approximation. Independence and uniqueness of a mathematical result cannot be certified by search alone; the literature assessment is limited to the works inspected and targeted searches reported in `REVIEW.md` and `AUDIT.json`.

## References
1. H. Pal and B. Bhattacharjya, *Pretty Good State Transfer on Circulant Graphs*, Electronic Journal of Combinatorics **24** (2017), P2.23, DOI 10.37236/6388; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i2p23/pdf/.
2. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, and R. Werner, *Irrational quantum walks*, first arXiv version 2022-08-18, arXiv:2208.08971, primary MSC 81P68; https://arxiv.org/html/2208.08971v1.
3. S. Kirkland and H. Monterde, *Quantum walks on join graphs*, first arXiv version 2023-12-12, arXiv:2312.06906; https://arxiv.org/html/2312.06906v1.
