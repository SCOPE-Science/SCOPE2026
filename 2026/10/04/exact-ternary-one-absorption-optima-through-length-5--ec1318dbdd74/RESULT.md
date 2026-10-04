# Exact ternary one-absorption optima through length \(5\)
## Finding
For the ternary alphabet \(\Sigma_3=\{0,1,2\}\), define a single absorption exactly as in Ye and Elishco: either adjacent symbols \(a,b\) are replaced by \(a\oplus b=\min(a+b,2)\), or the final symbol is missing. Let \(A^{ab}_3(n,1)\) denote the maximum size of a length-\(n\) one-absorption-correcting code, equivalently a family whose single-absorption balls are pairwise disjoint. Then
\[
A^{ab}_3(2,1)=3,\qquad A^{ab}_3(3,1)=6,\qquad A^{ab}_3(4,1)=13,\qquad A^{ab}_3(5,1)=29.
\]
An explicit optimal length-\(5\) code is
\[
\begin{aligned}
\{&00000,00011,00100,00121,00200,00222,01011,01102,01220,02010,\\
&02111,10000,10010,10021,10120,10222,11001,11101,11211,12100,\\
&12121,20000,20021,20110,20122,21200,22102,22201,22222\}.
\end{aligned}
\]
## Assumptions and scope
The claim is finite and exact. It concerns one absorption, alphabet \(\Sigma_3\), and blocklengths \(2\le n\le5\). The channel includes the terminal-missing case in the source definition. No statement is made for larger blocklengths, multiple absorptions, or other alphabets.
## Proof
For fixed \(n\), form every source word \(x\in\Sigma_3^n\) and its distinct single-absorption ball \(B(x)\subseteq\Sigma_3^{n-1}\). A correcting code is exactly a set of source words whose balls are pairwise disjoint. Therefore its maximum size is the optimum of the finite zero-one set-packing problem
\[
\max \sum_x z_x \quad\text{subject to}\quad \sum_{x:\,y\in B(x)} z_x\le1\quad (y\in\Sigma_3^{n-1}),\qquad z_x\in\{0,1\}.
\]
The bundled verifier builds this matrix directly from the channel definition and solves it to proven mixed-integer optimality for \(n=2,3,4,5\), obtaining \(3,6,13,29\). As an independent formulation, it also builds the conflict graph on \(\Sigma_3^n\), joins two source words precisely when their balls intersect, and solves the maximum-independent-set integer program with one inequality per conflict edge. The two formulations return the same four optima with zero reported MIP gap. The displayed codes, and the smaller witnesses in `optimal_codes.json`, are checked directly by set intersection and attain each bound.
## Verification
Run `python verify.py`. It reconstructs every ball from the definition, checks the explicit witnesses, solves both exact zero-one formulations for all four lengths, and prints `VERIFY_OK`. The checked environment used Python \(3\) with SciPy \(1.17.0\) and the bundled HiGHS mixed-integer backend.
## Relationship to prior work
Ye and Elishco introduced the absorption channel, defined the same single-absorption balls, and concentrated on low-redundancy constructions and asymptotic optimality. Their first public arXiv version is dated 2023-02-20. The accessible full text inspected for this result defines the channel and coding criterion but does not state these four finite ternary optima. A 2024 follow-up by Nguyen, Cai, Quek, and Immink improves ternary and general nonbinary redundancy constructions; its accessible abstract likewise states asymptotic redundancy results rather than these exact blocklengths. No inspected published source states the four exact finite optima.
## Limitations
The upper bounds are computer-assisted finite proofs using two exact integer formulations solved by HiGHS; they are not formal proof-assistant certificates. The follow-up 2024 conference paper was only available through abstract/metadata during the comparison, so an uninspected finite table there remains a residual originality risk, although its stated contribution is asymptotic construction. No claim is made beyond \(n=5\).
## References
1. Z. Ye and O. Elishco, “Codes Over Absorption Channels,” arXiv:2302.09842v1, first public 2023-02-20; later IEEE Transactions on Information Theory 70(6), 3981–4001 (2024), DOI 10.1109/TIT.2023.3346882.
2. T. T. Nguyen, K. Cai, T. Q. S. Quek, and K. A. S. Immink, “Efficient Constructions of Non-Binary Codes Over Absorption Channels,” IEEE ISIT 2024, 1718–1723, DOI 10.1109/ISIT57864.2024.10619179.
