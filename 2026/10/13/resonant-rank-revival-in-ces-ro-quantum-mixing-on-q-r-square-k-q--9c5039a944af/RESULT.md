# Resonant rank revival in Cesàro quantum mixing on \(Q_r\square K_q\)

## Finding
For all integers \(r\ge1\) and \(q\ge3\), the ordinary adjacency quantum walk on the mixed Hamming graph \(G_{r,q}=Q_r\square K_q\) has an exactly computable long-time average mixing spectrum. The rank exhibits a sharp arithmetic resonance:
\[
\operatorname{rank}\widehat M(G_{r,q})
=q2^{r-1}+(q-1)\mathbf 1_{\{q\equiv2\pmod4\}}
\sum_{\substack{q/2\le j\le r\\j\text{ odd}}}\binom rj.
\]
The empty sum is zero. Thus the rank equals half the \(q2^r\) vertices unless \(q\equiv2\pmod4\) and \(r\ge q/2\). In that exceptional regime additional nonconstant modes survive Cesàro averaging. In the first example, \(Q_3\square K_6\), the rank is \(29\) rather than \(24\) on \(48\) vertices.

## Assumptions and scope
The graph is simple, unweighted and connected. \(Q_r=K_2^{\square r}\); \(K_q\) is the simple complete graph, with \(q\ge3\). Its adjacency Hamiltonian is \(A=A(Q_r)\otimes I_q+I_{2^r}\otimes A(K_q)\). The instantaneous mixing matrix is \(M(t)=e^{itA}\circ e^{-itA}\), where \(\circ\) denotes entrywise multiplication. The ordinary Cesàro average is \(\widehat M=\lim_{T\to\infty}T^{-1}\int_0^T M(t)dt\). It exists because the spectrum is finite. We do not substitute an independently chosen time for each Cartesian factor.

For every integer \(0\le j\le r\), define
\[
c_j=\begin{cases}2^{-j}\binom j{j/2},&j\text{ even},\\0,&j\text{ odd}.
\end{cases}
\]
Let \(b_{j,q}=2^{-j}\binom j{(j-q/2)/2}\) when \(q\) is even, \(q/2\le j\) and \(j\equiv q/2\pmod2\); otherwise let \(b_{j,q}=0\). The complete indexed spectral list is
\[
\lambda_{j,0}=c_j\quad(\text{multiplicity }\binom rj),\qquad
\lambda_{j,1}=\frac{q-2}{q}c_j+\frac2q b_{j,q}
\quad(\text{multiplicity }(q-1)\binom rj).
\]
Coincident entries in this list are combined to obtain ordinary eigenvalue multiplicities. Every term is nonnegative.

## Proof
For \(K_2\), direct exponentiation shows that its instantaneous mixing matrix has eigenvalues \(1\) on constants and \(\cos(2t)\) on the orthogonal one-dimensional space. For \(K_q\), the identity
\[
A(K_q)=J_q-I_q
\]
gives a constant-sector mixing eigenvalue \(1\) and a standard-sector mixing eigenvalue
\[
a_q(t)=\frac{q-2+2\cos(qt)}q.
\]
Because the Cartesian adjacency summands commute, \(e^{itA}=e^{itA(Q_r)}\otimes e^{itA(K_q)}\), whence \(M(t)=M_{K_2}(t)^{\otimes r}\otimes M_{K_q}(t)\). The cube has \(\binom rj\) Walsh characters of weight \(j\), and the standard sector of \(K_q\) has dimension \(q-1\). On their common time-independent tensor eigenspaces, the instantaneous mixing eigenvalues are \(\cos^j(2t)\) and \(\cos^j(2t)a_q(t)\), with precisely the indexed multiplicities above. No claim of independence between their times is used.

All these trigonometric polynomials have integer frequencies and period dividing \(2\pi\). Consequently Cesàro averaging equals taking the constant Fourier coefficient. The binomial expansion
\[
\cos^j(2t)=2^{-j}\sum_{k=0}^j\binom jk e^{2i(j-2k)t}
\]
has constant term \(c_j\). Multiplication by \(2\cos(qt)=e^{iqt}+e^{-iqt}\) contributes a constant term exactly when \(2(j-2k)=\pm q\). Such a \(k\) exists exactly for even \(q\), \(q/2\le j\) and \(j\equiv q/2\pmod2\); the two symmetric contributions sum to \(2b_{j,q}\). This proves the complete spectral formulas, including positivity.

For \(j\) even, \(c_j>0\), and since \(q\ge3\), both indexed eigenvalues are strictly positive. For \(j\) odd, \(c_j=0\), so the cube-constant component vanishes. Its standard-\(K_q\) counterpart survives if and only if \(q/2\) is odd and \(q/2\le j\), equivalently \(q\equiv2\pmod4\) and \(j\ge q/2\). The number of even-weight cube characters is \(\sum_{j\text{ even}}\binom rj=2^{r-1}\). Weighting all even sectors by the total \(1+(q-1)=q\) dimensions, and adding precisely the surviving odd standard sectors, yields the rank formula. For \(q=6,r=3\), the coefficient on \(j=3\) is \(2\binom30/(6\cdot8)=1/24\), with multiplicity \(5\); thus \(24+5=29\).

## Verification
Run `python3 verify.py` with a standard Python 3 installation. It checks \(616\) exact rational indexed spectral coefficients and ranks for \(1\le r\le8\) and \(q\in\{3,4,5,6,8,10,14\}\). More importantly, it independently builds spectral projectors of the adjacency Hamiltonians by Walsh/Krawtchouk idempotents and complete-graph projectors, merges equal total energies, forms \(\sum_\theta E_\theta\circ E_\theta\), and computes exact rational matrix ranks for five graph orders through \(96\) vertices. The verifier directly checks rank \(29\) of \(Q_3\square K_6\). These finite tests are independent crosschecks and not the proof for arbitrary parameters; the full proof is the Fourier identity above.

## Relationship to prior work
Godsil's foundational average-mixing formula expresses the Cesàro matrix as the sum of Schur squares of adjacency spectral projections [1]. Coutinho, Godsil, Guo and Zhan study rank and the commutant interpretation of that matrix [2]. Lo and collaborators study Cartesian quantum-walk bunkbeds, including a single \(P_2\) factor with a circulant, as an average-mixing problem [3]. Coutinho and collaborators develop exact algebraic methods for average quantum mixing [4]. The 2024 survey discusses rank and eigenvalues as motivated structural questions [5].

Those general tools and the already-known homogeneous Hamming/cube special cases do not themselves state this mixed-alphabet rank transition. The key new comparison is at coincident Fourier frequencies: the \(q\equiv2\pmod4\) resonance restores positive odd-weight eigenvalues only when the binary dimension reaches \(q/2\). The explicit closed rank law, rather than a computation on any fixed finite graph, is the assessed statement. Literature completeness is not guaranteed.

## Limitations
The result concerns unweighted adjacency evolution and the ordinary uniform Cesàro time average, not optimally chosen random observation times. It does not classify arbitrary products of multiple unequal complete graphs or signed/chiral Hamiltonians. The exact count of distinct eigenvalues is not claimed where indexed eigenvalues coincide. A general published Cartesian-product theorem phrased in terms of Fourier frequency collisions might subsume this special family; the primary sources checked below did not provide the exact rank law.

## References
[1] C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, especially Lemma 1.1 and spectral examples. https://arxiv.org/abs/1103.2578

[2] G. Coutinho, C. Godsil, K. Guo and H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, especially Sections 3--6. https://arxiv.org/abs/1709.03591

[3] P. Lo et al., *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059, especially Section 5. https://arxiv.org/abs/quant-ph/0509059

[4] G. Coutinho et al., *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18; primary MSC 81P68 in the journal record), especially Section 2. https://arxiv.org/abs/2208.08971

[5] G. Coutinho and K. Guo, *Selected open problems in continuous-time quantum walks*, *Special Matrices* 12 (2024), DOI:10.1515/spma-2024-0025, Section 4. https://doi.org/10.1515/spma-2024-0025
