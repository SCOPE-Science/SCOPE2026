# Consecutive Fourier bands minimize primitive-row frame potential at every modulus

## Finding
For every integer \(N\ge2\) and number of frequencies \(1\le s\le N\), consider the \(\varphi(N)\)-dimensional unit vectors
\[
 v_a=\frac1{\sqrt{\varphi(N)}}\left(e^{2\pi i au/N}\right)_{u\in U_N},\qquad U_N=\{u\in\mathbb Z/N\mathbb Z:\gcd(u,N)=1\}.
\]
For each \(s\)-element subset \(A\subseteq\mathbb Z/N\mathbb Z\), let \(\mathrm{FP}(A)=\sum_{a,b\in A}|\langle v_a,v_b\rangle|^2\). This is the aggregate squared inner-product energy of the selected columns of the primitive-row Fourier matrix.

Let \(\mathcal P_N\) be the set of distinct prime divisors of \(N\). For each \(p\in\mathcal P_N\), write \(p^{k_p}\Vert N\), \(\beta_p=(p-1)^{-2}\), and \(\gamma_p=1-\beta_p\). For \(S\subseteq\mathcal P_N\), set
\[
 d_S=\prod_{p\in\mathcal P_N}p^{k_p-1+\mathbf1_{p\in S}},\qquad
 w_S=\prod_{p\in S}\gamma_p\prod_{p\in\mathcal P_N\setminus S}\beta_p.
\]
All weights are nonnegative, their sum is one, and for \(p=2\) we have \(\gamma_2=0\). Given a positive integer \(d\), write \(s=dq+r\) with \(0\le r<d\), and define \(B_d(s)=dq^2+r(2q+1)\).

**Sharp minimum:**
\[
 \boxed{\min_{|A|=s}\mathrm{FP}(A)=\sum_{S\subseteq\mathcal P_N}w_SB_{d_S}(s).}
\]
Every cyclic interval \(A=\{t,t+1,\ldots,t+s-1\}\pmod N\) is a minimizer, including its image under any multiplication by a unit modulo \(N\).

**Complete equality test and deficit:** For \(d\mid N\) and residue \(r\), put \(m_{d,r}=|\{a\in A:a\equiv r\pmod d\}|\) and \(q_d=\lfloor s/d\rfloor\). Then
\[
 \boxed{\mathrm{FP}(A)-\mathrm{FP}_{\min}=\sum_{S\subseteq\mathcal P_N}w_S\sum_{r=0}^{d_S-1}(m_{d_S,r}-q_{d_S})(m_{d_S,r}-q_{d_S}-1).}
\]
Every summand is nonnegative for integer multiplicities. Thus \(A\) is optimal **if and only if** for each \(S\) with \(w_S>0\), every residue modulo \(d_S\) is occupied either \(q_{d_S}\) or \(q_{d_S}+1\) times. This classifies all minimizers by simultaneous modular balance without claiming that consecutive intervals are the only ones.

## Assumptions and scope
All scalar products are the usual Hermitian inner product in \(\mathbb C^{\varphi(N)}\), with every Fourier column divided by \(\sqrt{\varphi(N)}\). The frequency set is a genuine subset, not a multiset; \(s\) is any integer between one and \(N\) inclusive. The rows are precisely the **unit residue classes** modulo \(N\), not an additive subgroup in general. The result optimizes only the stated squared-pair-potential over choice of \(A\); it does not optimize the maximum individual coherence, the operator condition number, or reconstruction error.

## Proof
**1. Character sums and normalization.** If \(c_N(h)=\sum_{u\in U_N}e^{2\pi iuh/N}\) is the Ramanujan sum, orthogonality of phases gives \(\langle v_a,v_b\rangle=c_N(b-a)/\varphi(N)\). Its conjugation sign is immaterial after squaring. The Chinese remainder theorem makes both \(c_N\) and \(\varphi\) multiplicative in coprime factors, so the normalized squared Gram kernel factors over prime powers.

**2. Exact nonnegative local decomposition.** For \(p^k\Vert N\), the prime-power Ramanujan identity is
\[
 c_{p^k}(h)=\begin{cases}p^{k-1}(p-1),&p^k\mid h,\\-p^{k-1},&p^{k-1}\mid h\text{ but }p^k\nmid h,\\0,&p^{k-1}\nmid h.\end{cases}
\]
This follows directly by subtracting the full geometric sum over multiples of \(1\) from the sum over multiples of \(p\): \(c_{p^k}(h)=\sum_{x\bmod p^k}e^{2\pi ixh/p^k}-\sum_{y\bmod p^{k-1}}e^{2\pi i pyh/p^k}\). Since \(\varphi(p^k)=p^{k-1}(p-1)\), it follows for every integer \(h\) that
\[
 \left|\frac{c_{p^k}(h)}{\varphi(p^k)}\right|^2=\beta_p\mathbf1_{p^{k-1}\mid h}+\gamma_p\mathbf1_{p^k\mid h}.
\]
This identity also includes \(p=2\) and \(k=1\): the first indicator then means divisibility by one and \(\gamma_2=0\). Multiplying these nonnegative factors and distributing yields
\[
 |c_N(h)/\varphi(N)|^2=\sum_{S\subseteq\mathcal P_N}w_S\mathbf1_{d_S\mid h}.
\]

**3. Residue-count energy.** Summing over the ordered pairs \((a,b)\in A^2\) gives exactly
\[
 \mathrm{FP}(A)=\sum_Sw_S\sum_{r=0}^{d_S-1}m_{d_S,r}^2.
\]
For any modulus \(d\), the integers \(m_r\ge0\) sum to \(s\). The convexity of the square (or replacement of two entries differing by at least two by their mean-adjacent integers) shows \(\sum_rm_r^2\ge B_d(s)\), with equality exactly when each \(m_r\in\{\lfloor s/d\rfloor,\lceil s/d\rceil\}\). There is also the **exact identity**
\[
 \sum_rm_r^2-B_d(s)=\sum_r(m_r-q_d)(m_r-q_d-1),
\]
whose right-hand terms are all nonnegative integers since products of consecutive integers are never negative.

**4. Simultaneous sharpness and equality.** A consecutive \(s\)-element cyclic interval has balanced counts modulo **every** divisor \(d\mid N\): division of \(s\) by \(d\) gives each residue \(q_d\) or \(q_d+1\) occurrences. It therefore realizes every individual lower bound from step 3 at once. This proves the minimum formula. Summing the exact nonnegative deficits proves the displayed deficit and the equality classification. When \(\gamma_2=0\), conditions with zero weight must not be imposed; their omission is essential for the general even-modulus statement. Unitary dilation \(A\mapsto uA\) simply permutes residue classes for every \(d\mid N\) and preserves all counts up to relabeling.

## Verification
The standard-library checker `verify.py` independently computes each Ramanujan sum by its integer divisor/Möbius formula, computes \(\mathrm{FP}(A)\) directly from the full pair list, and compares it with the weighted residue formula and sharp-value/deficit formulas. It exhaustively enumerates small subsets, verifies the complete equality criterion, and tests representative prime powers and mixed composite moduli. Invoke `python verify.py` from the package directory. Its successful check is supplementary evidence; the proof above applies to all \(N\ge2\) and all allowed \(s\).

For an exact example, take \(N=9\) and \(s=4\). The only nonzero weights are \(w_{\varnothing}=1/4\) for \(d=3\) and \(w_{\{3\}}=3/4\) for \(d=9\), so the minimum is \((1/4)B_3(4)+(3/4)B_9(4)=9/2\). A consecutive four-element set attains \(9/2\), whereas \(A=\{0,1,3,6\}\) has potential \(11/2\). The strictly positive deficit detects its three frequencies in one residue class modulo three.

## Relationship to prior work
The classical Benedetto–Fickus frame potential and its generalizations characterize unconstrained or structured tight-frame minima, but do not by themselves solve the discrete selection problem when rows of a fixed Fourier matrix are restricted to unit residues and only frequency columns may vary. Johnson–Okoudjou study translation-generated frames sampled over an **additive subgroup** of a finite abelian group, together with conditions for tightness; \(U_N\) is ordinarily not an additive subgroup, and their assertions do not imply the present all-size, all-modulus optimum and equality-deficit formula. Vaidyanathan studies Ramanujan sums in finite-periodic signal processing, supplying relevant harmonic-analysis context rather than frequency-subset frame-potential optimization. Mixon–Needham–Shonkwiler–Villar explain the general Benedetto–Fickus theorem and its unconstrained frame geometry. The arithmetic nonnegative-kernel decomposition and the simultaneous modular-balance optimization are the additional ingredients needed here.

## Limitations
The result is confined to the squared frame potential of columns of a **fixed, primitive-row** Fourier submatrix; it does not prove optimal RIP constants, low mutual coherence, robustness to noise, or a characterization of all tight frames. All normalizations and the zero-weight \(2\)-adic case are included in the proof. The literature comparison does not rule out an equivalent formulation in older harmonic-frame design literature; exhaustive historical priority is not certified. No external audit is asserted.

## References
1. B. D. Johnson and K. A. Okoudjou, *Frame Potential and Finite Abelian Groups*, arXiv:0801.3813 (first public preprint 2008-01-24), especially §§1 and 4.
2. P. P. Vaidyanathan, *Ramanujan-Sum Expansions for Finite Duration (FIR) Sequences*, available at https://systems.caltech.edu/dsp/PPVSquare.pdf, §§I–IV.
3. P. P. Vaidyanathan, *Ramanujan Sums in the Context of Signal Processing—Part I: Fundamentals*, IEEE Trans. Signal Process. 62 (2014), 4145–4157, DOI: 10.1109/TSP.2014.2331617.
4. D. G. Mixon, T. Needham, C. Shonkwiler, and S. Villar, *Three Proofs of the Benedetto–Fickus Theorem*, arXiv:2112.02916, §§1–4.
5. M. Fickus, B. D. Johnson, K. Kornelson, and K. A. Okoudjou, *Convolutional Frames and the Frame Potential*, Appl. Comput. Harmon. Anal. 19 (2005), 77–91, DOI: 10.1016/j.acha.2005.02.005.
