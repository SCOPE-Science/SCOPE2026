# The eightfold inverse-diffraction ambiguity of the Grigorchuk Toeplitz subshift

## Finding
Consider the four-letter substitution \(\tau(a)=aca\), \(\tau(b)=d\), \(\tau(c)=b\), \(\tau(d)=c\), and its uniquely ergodic bilateral subshift. Attach arbitrary **real** scattering weights \((A,B,C,D)\in\mathbb R^4\) to the respective letters and form the weighted lattice Dirac comb. The entire kinematic diffraction measure is determined by just five representative Bragg intensities, at frequencies \(0,1/2,1/4,1/8,1/16\).

Define the following invertible real-linear coordinates:
\[
\begin{aligned}
M&=(7A+2B+4C+D)/14,\\
V&=-A+(2B+4C+D)/7,\\
P&=(4B-6C+2D)/7,\\
Q&=(-6B+2C+4D)/7,\\
R&=(2B+4C-6D)/7=-P-Q.
\end{aligned}
\]
For each reduced dyadic frequency \(m/2^r\) with \(m\) odd and \(r\ge1\), its diffraction intensity, independent of the odd numerator, is
\[
I_r=\begin{cases}
V^2/4,&r=1,\\
4^{-r}P^2,&r\ge2,\ r\equiv2\pmod3,\\
4^{-r}Q^2,&r\ge2,\ r\equiv0\pmod3,\\
4^{-r}R^2,&r\ge2,\ r\equiv1\pmod3.
\end{cases}
\]
Every integer-frequency Bragg peak has intensity \(I_0=M^2\); all other frequencies have zero diffraction measure, so the diffraction is pure point and periodic modulo the integer lattice.

**Exact inverse classification.** Two real weight vectors have the same full diffraction measure if and only if their \(M\) and \(V\) coordinates agree up to *independent* signs and their \((P,Q)\) pairs agree up to a *single common* sign. For fixed \((M,V,P,Q)\), all homometric weightings are given by
\[
(A',B',C',D')=
\left(M'-\frac{V'}2,\quad M'+\frac{V'}2+\frac{P'-Q'}2,\quad
M'+\frac{V'}2-\frac{P'}2,\quad M'+\frac{V'}2+P'+Q'\right),
\]
where \((M',V',P',Q')=(\epsilon_0M,\epsilon_1V,\epsilon_2P,\epsilon_2Q)\) and each \(\epsilon_j\in\{-1,1\}\). Consequently a generic real weighting has **exactly eight** diffraction-indistinguishable real weightings. More generally, the fiber cardinality is
\[
2^{\mathbf1_{M\ne0}+\mathbf1_{V\ne0}+\mathbf1_{(P,Q)\ne(0,0)}}.
\]
Even when all four letter weights are required to be **strictly positive and mutually distinct**, nontrivial ambiguity survives: the following four weight vectors are all positive, have pairwise distinct entries, and have exactly the same *full* diffraction measure:
\[
(10,11,13,14),\quad
(10,99/7,85/7,78/7),\quad
(88/7,59/7,73/7,80/7),\quad
(88/7,81/7,67/7,60/7).
\]
They are not obtained from one another merely by relabeling the four weights. Phase-resolved (signed) values of \(M,V,P,Q\), unlike their squared magnitudes, uniquely recover the labeled weights.

## Assumptions and scope
The substitution fixed point starts with \(a\); its letters at zero-based positions \(n\ge0\) are \(a\) when \(\nu_2(n+1)=0\) and, when \(\nu_2(n+1)\ge1\), repeat \(c,b,d\) as the valuation increases by one. This follows by induction on substitution words. We use the canonical uniquely ergodic bilateral hull, and associate \(\omega=\sum_{n\in\mathbb Z}w_n\delta_n\) to a point in that hull. Autocorrelations are volume-normalized limits of \((2N+1)^{-1}\sum_{n=-N}^N w_nw_{n-h}\). The diffraction is their Fourier transform, using frequency convention \(e^{-2\pi i qn}\). A different hull point yields the same measure by unique ergodicity. The theorem concerns arbitrary real weights, not arbitrary complex scattering factors or an inverse problem in which the symbolic substitution is itself unknown.

## Proof
**(1) Exact valuation coding and Haar model.** The substitution produces words \(\tau^k(a)\) of length \(2^{k+1}-1\), with \(a\) at every even position. Their odd-position skeleton is recursively the letter cycle \(c\to b\to d\to c\). Induction gives the stated valuation formula. Identify the uniquely invariant measure with Haar probability on \(\mathbb Z_2\), as furnished by the dyadic-odometer description of this subshift. Define \(u_0=A\), and \(u_1=C,u_2=B,u_3=D,u_4=C,\ldots\). The associated observable at a two-adic integer \(x\ne-1\) is \(u_{\nu_2(x+1)}\). The point \(x=-1\) is Haar-null and may be defined arbitrarily. Its finite-level periodic approximants converge in \(L^2\), so the weighted lattice sequence has pure point diffraction with Fourier--Bohr peak intensities equal to squares of its Haar Fourier coefficients. The unique ergodicity of the hull supplies existence and independence of the autocorrelation limits.

**(2) Fourier coefficients on valuation shells.** Each shell \(S_k=\{x\in\mathbb Z_2:\nu_2(x)=k\}\) has Haar measure \(2^{-k-1}\). For an odd integer \(m\) and \(r\ge1\), integration of the character \(e^{-2\pi imx/2^r}\) over \(S_k\) gives \(0\) for \(k\le r-2\), \(-2^{-r}\) for \(k=r-1\), and \(2^{-k-1}\) for \(k\ge r\). Shifting \(x\) to \(x+1\) introduces only the unit phase \(e^{2\pi im/2^r}\). Thus the Fourier coefficient has magnitude
\[
2^{-r}\left|\sum_{j=0}^\infty2^{-j-1}u_{r+j}-u_{r-1}\right|.
\]
For \(r\ge1\), the tail is \((4u_r+2u_{r+1}+u_{r+2})/7\). At \(r=1\), the preceding letter is \(u_0=A\), yielding \(V\). For \(r\ge2\), \(u_{r-1}=u_{r+2}\), giving the three-cycle \((P,Q,R)\). The zero-character coefficient is \(M=(7A+2B+4C+D)/14\). As a normalization cross-check, summing all intensities in one Fourier period gives the exact Parseval identity
\[
M^2+V^2/4+P^2/7+Q^2/14+R^2/28=A^2/2+B^2/7+2C^2/7+D^2/14.
\]
Since the dual group of the dyadic odometer consists precisely of dyadic rational characters and these characters span \(L^2\), no continuous diffraction contribution is possible. The intensity formulas and five-peak sufficiency follow.

**(3) Inverse uniqueness.** Direct substitution verifies the stated inverse linear map; the forward map \((A,B,C,D)\mapsto(M,V,P,Q)\) has determinant \(-4/7\), so this inverse is unique. Equality of full diffraction gives equality of \(M^2,V^2,P^2,Q^2,R^2\), with \(P+Q+R=0\). If two real triples sum to zero and have pairwise matching absolute values, then they are equal up to one global sign: when nonzero, whichever coordinate has greatest magnitude equals the sum of the other two magnitudes, fixing the necessary relative signs; the all-zero and one-zero cases follow directly. Thus \((P',Q',R')=(P,Q,R)\) or \(-(P,Q,R)\), while \(M\) and \(V\) have independent sign freedoms. Conversely every such sign choice preserves all listed intensities, hence the entire diffraction. Counting the nontrivial sign choices proves the fiber formula, including its degenerate cases.

**(4) A positive, injective ambiguity.** The first displayed positive vector has \((M,V,P,Q,R)=(79/7,18/7,-6/7,16/7,-10/7)\), with all three independent sign freedoms present. Fix \(M\) and choose the two signs of \(V\) and \((P,Q)\) in the inverse formula. This gives exactly the four displayed positive, injectively weighted vectors, all with identical intensities. Their unordered multisets of weights differ, excluding a relabeling explanation.

## Verification
The standalone `verify.py` tests the substitution/valuation identity on a long exact prefix, all 625 integer vectors in a small four-parameter cube for exact inversion, and the three-step Bragg recurrence. It constructs the four positive and eight real ambiguities, verifies 25 dyadic peak intensities exactly for each, compares eight raw Fourier sums against the closed coefficients, and independently compares 33 finite cyclic autocorrelation lags. The verifier returned `VERIFY_OK`; the largest finite autocorrelation discrepancy was approximately \(0.00263074\) at periodic approximation length \(8192\), consistent with finite-level boundary errors. Exact infinite conclusions rest on the proofs above, not on these finite observations.

## Relationship to prior work
Vorobets (2009) established the Grigorchuk substitution's almost one-to-one dyadic-odometer model, unique ergodicity and pure point dynamical spectrum, but did not give the present all-real-weight diffraction inverse fibers. Baake and Grimm (2006, 2008) explained homometry and diffraction inverse problems generally; their planar model-set examples and mixed-spectrum constructions do not imply this explicit four-letter, eightfold fiber classification without the present valuation-shell computation. Baake and Grimm (2010) explicitly treated pure point diffraction of the *period-doubling* sequence and the planar chair structure, rather than this Grigorchuk substitution. These frameworks supply ingredients and motivation. The asserted contribution is the explicit Grigorchuk inverse classification, not the odometer or general pure-point diffraction principles.

## Limitations
This is an exact result for **real** fixed-letter weights and this specific canonical substitution; it does not classify complex weights, physically unknown substitutions, or recovery from noisy/finite-window data. The eightfold ambiguity counts labeled real vectors, including global sign; the four exhibited positive vectors show a residual nontrivial ambiguity without global sign. Existing general model-set methods may contain an implicit equivalent calculation not exposed by the inspected primary texts; historical priority has not been independently established. The finite numerical experiments cannot certify infinite Fourier support, which is established analytically by the odometer model.

## References
- Y. Vorobets, *On a substitution subshift related to the Grigorchuk group*, arXiv:0910.4800v1 (first publicly posted 2009-10-26), https://arxiv.org/abs/0910.4800.
- M. Baake and U. Grimm, *Homometric model sets and window covariograms*, arXiv:math/0610411v1 (first publicly posted 2006-10-12), https://arxiv.org/abs/math/0610411.
- U. Grimm and M. Baake, *Homometric point sets and inverse problems*, arXiv:0808.0094v1 (first publicly posted 2008-08-01), https://arxiv.org/abs/0808.0094.
- M. Baake and U. Grimm, *Diffraction of limit periodic point sets*, arXiv:1007.0707v1 (first publicly posted 2010-07-05), https://arxiv.org/abs/1007.0707.
