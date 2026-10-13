# Temperature-dual Dicke recovery: exact jump throughput and no-jump dephasing

## Finding

For every integer \(n\ge5\), every integer \(1\le a\le\lfloor(n-3)/2\rfloor\), and every excitation probability \(0\le p\le1\), the complementary-weight Dicke code with weights \(a\) and \(b=n-a\) has an explicit three-syndrome, trace-nonincreasing recovery for \(n\) independent generalized amplitude-damping (GAD) channels. Its conditional entanglement fidelity is \(1-O(\gamma^2)\) as the damping strength \(\gamma\downarrow0\). More precisely, uniformly over logical inputs to first order, the success probability is
\[
P_{\mathrm{succ}}(\gamma)=1-\gamma\left(s_{\max}-\frac{a(b+1)}n\right)+O(\gamma^2),\quad
s_{\max}=\max\{(1-p)a+pb,(1-p)b+pa\}.
\]
The sum of the accepted one-downward-jump and one-upward-jump probabilities is
\[
J(\gamma)=\gamma\,\frac{a(b+1)}n+O(\gamma^2),
\]
**independent of the bath parameter** \(p\). The two respective contributions are \((1-p)J\) and \(pJ\) at leading order. The coefficient \(a(b+1)/n\) is the largest common accepted single-jump coefficient in the specified Dicke-syndrome, diagonal-contraction recovery family; no global recovery optimum is asserted.

There is also an **exact finite-strength coherence factor** for the accepted no-jump sector in the specified thermal Kraus grouping. Put \(q=1-p\), and for integers \(0\le w,\ell\le n\) define
\[
f_{w,\ell}(\gamma)=\frac1{\binom nw}\sum_{t=\max(0,w-n+\ell)}^{\min(w,\ell)}\binom\ell t\binom{n-\ell}{w-t}(1-\gamma)^{(n-\ell-w+2t)/2}.
\]
Define \(M_{uv}(\gamma)=\sum_{\ell=0}^n\binom n\ell q^\ell p^{n-\ell}f_{u,\ell}(\gamma)f_{v,\ell}(\gamma)\). The normalized no-jump logical-coherence factor after projection and positive diagonal filtering is exactly
\[
D(\gamma)=\frac{M_{ab}(\gamma)}{\sqrt{M_{aa}(\gamma)M_{bb}(\gamma)}}.
\]
For \(0<\gamma<1\), it satisfies \(D=1\) at \(p\in\{0,1\}\), and \(0<D<1\) at every \(0<p<1\). Its sharp weak-damping law is
\[
\boxed{D(\gamma)=1-\frac{(b-a)^2p(1-p)}{2n}\gamma^2+O(\gamma^3).}
\]
This factor refers to the **no-jump subchannel only**, not to the full recovered logical channel. The theorem combines an exactly temperature-independent accepted jump coefficient with a precisely temperature-dependent residual no-jump dephasing coefficient.

Within this complementary-weight, three-syndrome family, increasing the smaller weight \(a\) **strictly increases** the accepted-jump coefficient and **weakly decreases** the no-jump decoherence coefficient (strictly for \(0<p<1\)). Both objectives are optimized at \(a=\lfloor(n-3)/2
floor\): the minimum admissible excitation gap is three for odd \(n\) and four for even \(n\). This is a restricted-family Pareto statement, not a global code-design optimum.

## Assumptions and scope

The normalized symmetric Dicke vector is \(\lvert D_n^w\rangle=\binom nw^{-1/2}\sum_{x\in\{0,1\}^n:\,|x|=w}\lvert x\rangle\). Encode \(\lvert0_L\rangle=\lvert D_n^a\rangle\) and \(\lvert1_L\rangle=\lvert D_n^b\rangle\). The excitation gap \(b-a\ge3\) makes the three unordered pairs of excitation weights \(\{a,b\}\), \(\{a-1,b-1\}\), \(\{a+1,b+1\}\) mutually disjoint.

On one qubit, use the four Kraus operators
\[
A_0=\sqrt{1-p}\,\operatorname{diag}(1,\sqrt{1-\gamma}),\quad A_1=\sqrt{(1-p)\gamma}\lvert0\rangle\langle1\rvert,\quad
B_0=\sqrt p\,\operatorname{diag}(\sqrt{1-\gamma},1),\quad B_1=\sqrt{p\gamma}\lvert1\rangle\langle0\rvert.
\]
They act independently on every physical qubit. Here \(p\in[0,1]\) is the excited-state equilibrium population; a passive, non-inverted thermal bath has \(p\in[0,1/2]\). All expansions are for fixed \(n,a,p\) as \(\gamma\to0^+\). For the prescribed recovery, \(\gamma\) is sufficiently small that the displayed filters are contractions.

## Proof

**1. Explicit recovery and completely positive trace-nonincreasing property.** Define \(s_w=(1-p)w+p(n-w)\), \(s_{\max}=\max(s_a,s_b)\), and \(\xi=\sqrt{a(b+1)/(b(a+1))}\in(0,1)\). The following operators act from the physical Hilbert space back to the two-dimensional codespace:
\[
R_0=\sum_{w\in\{a,b\}}\left[1-\frac\gamma2(s_{\max}-s_w)\right]\lvert D_n^w\rangle\langle D_n^w\rvert,
\]
\[
R_-=\lvert D_n^a\rangle\langle D_n^{a-1}\rvert+\xi\lvert D_n^b\rangle\langle D_n^{b-1}\rvert,
\qquad
R_+=\xi\lvert D_n^a\rangle\langle D_n^{a+1}\rvert+\lvert D_n^b\rangle\langle D_n^{b+1}\rvert.
\]
Their initial supports are mutually orthogonal, and each singular value is at most one for small enough \(\gamma\); hence \(\sum_{\epsilon\in\{0,-,+\}}R_\epsilon^\dagger R_\epsilon\preceq I\). They implement a valid postselected recovery, and other outcomes are rejected.

**2. Leading jump amplitudes.** For a fixed site \(i\), symmetry and binomial overlap give
\[
\langle D_n^{w-1}\rvert\sigma_i^-\lvert D_n^w\rangle=\frac{\sqrt{w(n-w+1)}}n,
\qquad
\langle D_n^{w+1}\rvert\sigma_i^+\lvert D_n^w\rangle=\frac{\sqrt{(n-w)(w+1)}}n.
\]
For the complementary weights the two downward coefficients are \(\sqrt{a(b+1)}/n\) and \(\sqrt{b(a+1)}/n\), with the order reversed in the upward sector. Multiplication by \(\xi\) equalizes both components at \(\sqrt{a(b+1)}/n\). There are \(n\) possible jump sites, and summing the non-jump Kraus patterns on the remaining sites gives unit total probability to leading order. Thus the accepted downward and upward subchannels are respectively
\[
\gamma(1-p)\frac{a(b+1)}n\rho+O(\gamma^2),\qquad
\gamma p\frac{a(b+1)}n\rho+O(\gamma^2).
\]
The filters cannot equalize both logical amplitudes at a coefficient greater than the smaller unfiltered overlap while remaining contractions; this proves the limited branchwise optimum stated above.

**3. The no-jump branch and the success probability.** A tensor product containing only \(A_0,B_0\) has probability prefactor \((1-p)^{\ell/2}p^{(n-\ell)/2}\) when \(\ell\) sites carry \(A_0\). Its projection between weight-\(w\) Dicke states has scalar \(f_{w,\ell}(\gamma)\). At first order, the pattern-average across \(\ell\) gives \(1-\gamma s_w/2+O(\gamma^2)\) at logical amplitude level, and the factor in \(R_0\) makes both logical amplitudes equal to \(1-\gamma s_{\max}/2+O(\gamma^2)\). Summing accepted Kraus branches gives the scalar logical map
\[
\rho\longmapsto\left[1-\gamma s_{\max}+\gamma\frac{a(b+1)}n\right]\rho+O(\gamma^2).
\]
Branches with two or more physical jumps have probability \(O(\gamma^2)\); rejected nonsymmetric portions of no-jump states also contribute only at second order. It follows that postselection succeeds with the displayed probability for every logical input through order \(\gamma\), and the normalized entanglement fidelity on a maximally entangled logical-reference input is \(1-O(\gamma^2)\). This is not a claim of exact correction at finite \(\gamma\).

**4. Exact no-jump coherence and strictness.** If a no-jump Kraus pattern has \(\ell\) occurrences of \(A_0\), a weight-\(w\) basis string with \(t\) excitations on these positions gains precisely \(n-\ell-w+2t\) factors \(\sqrt{1-\gamma}\). Hypergeometric counting yields \(f_{w,\ell}\). Averaging the overlap of the two projected amplitudes over all patterns proves the exact expression for \(M_{uv}\). Positive diagonal filtering multiplies each logical amplitude by a factor depending only on \(w\), so cancels from \(D\). Cauchy–Schwarz gives \(0<D\le1\). At \(p=0\) or \(p=1\) exactly one \(\ell\) contributes, hence equality. For \(0<p<1\), both \(\ell=0\) and \(\ell=n\) occur with positive weight. Their ratios \(f_{a,\ell}/f_{b,\ell}\) are respectively \((1-\gamma)^{(b-a)/2}\) and \((1-\gamma)^{-(b-a)/2}\), which differ for \(0<\gamma<1\); thus equality is impossible.

**5. Quadratic coherence coefficient.** Differentiate the hypergeometric average at \(\gamma=0\):
\[
f_{w,\ell}(\gamma)=1-\frac\gamma2 h_w(\ell)+O(\gamma^2),\qquad
h_w(\ell)=\frac{w\ell+(n-w)(n-\ell)}n.
\]
If \(L\sim\operatorname{Bin}(n,1-p)\), the exact normalized overlap is the cosine of the angle between two vectors indexed by \(L\), weighted by its binomial probability. Expanding normalized vectors gives
\[
1-D(\gamma)=\frac{\gamma^2}{8}\operatorname{Var}[h_a(L)-h_b(L)]+O(\gamma^3).
\]
Here \(h_a(\ell)-h_b(\ell)\) is affine in \(\ell\) with slope \(-2(b-a)/n\), and \(\operatorname{Var}(L)=np(1-p)\). Therefore the variance is \(4(b-a)^2p(1-p)/n\), yielding the claimed coefficient.

**6. Restricted-family tradeoff.** The difference in jump coefficients upon replacing \(a\) with \(a+1\) is \((n-2a)/n>0\); the coherence-loss coefficient weakly decreases (strictly when \(0<p<1\)) because the excitation gap \(n-2a\) decreases by two. The largest admissible \(a\) therefore optimizes both objectives within the stated class, with minimum gap three (odd length) or four (even length).

## Verification

The standalone `verify.py` (Python 3.10+, NumPy; `requirements.txt`) checks the binomial variance identity in exact rational arithmetic for all admissible weight pairs up to \(n=24\), at six rational bath parameters. It also evaluates the exact hypergeometric no-jump formula and checks direct full Kraus-matrix channel/recovery compositions for two code lengths at two damping strengths. The executed script returned `VERIFY_OK 1348 exact/combinatorial and full-Kraus checks`. These finite checks are consistency evidence, not a substitute for the all-size argument in the proof.

## Relationship to prior work

Dutta, Rudra, Seksaria, Prabhakar and Mandayam (2026), arXiv:2609.15924v1, construct the five-qubit weight-\(1\)/weight-\(4\) Dicke code, introduce probabilistic approximate quantum error correction for GAD noise, and derive general recovery and finite-five-qubit fidelity expressions. Those achievements, and the general observation that suitable postselection can remove first-order infidelity, are **not** claimed as new. The present theorem supplies a concrete symmetric-Dicke-projection recovery for **every admissible complementary-weight pair and size**, an explicit temperature-independent accepted-jump coefficient, a full leading acceptance law, and an exact finite-strength no-jump coherence invariant with a sharp coefficient and strict finite-temperature criterion. Their general PAQEC expressions could in principle be specialized to this restricted recovery; no theorem about global optimality over recovery channels is made.

Dutta, Jain and Mandayam (2026), arXiv:2410.00155, present probabilistic amplitude-damping codes at zero temperature. Ouyang and Chao (2018), arXiv:1809.09801, develop permutation-invariant **constant-excitation bosonic** amplitude-damping codes. Cafaro and van Loock (2014), arXiv:1308.4582, analyze approximate QEC for finite-temperature GAD with other stabilizer/nonadditive code families. These works supply related construction and channel context without stating the exact two-weight, all-size invariant classified here in the inspected material.

## Limitations

The exact \(D\) formula is for the normalized **accepted no-jump subchannel under the stated physical Kraus decomposition**, not for the normalized sum of all recovered error sectors or a Kraus-representation-independent observable. Success and accepted-jump expressions are asymptotic, not finite-strength equalities. The recovery is a specified three-syndrome projection that discards components outside three symmetric two-dimensional subspaces, and it is not shown optimal among unrestricted recoveries. Only independent, identically parameterized GAD qubit channels are covered. The bound \(1-O(\gamma^2)\) holds at fixed \(n\); no claim of uniform error control as \(n\to\infty\) with \(n\gamma\) fixed is made. The closest 2026 five-qubit construction provides a generic formalism, so implicit or future specialization of that formalism is an originality risk.

## References

1. S. Dutta, A. Rudra, M. Seksaria, A. Prabhakar, P. Mandayam, *Quantum Codes for Generalized Amplitude-damping Noise*, arXiv:2609.15924v1 (2026-09-14), https://arxiv.org/pdf/2609.15924.
2. S. Dutta, A. Jain, P. Mandayam, *Smallest quantum codes for amplitude-damping noise*, arXiv:2410.00155; Phys. Rev. Research 8, L032004 (2026), https://doi.org/10.1103/6g5l-m4r1.
3. Y. Ouyang, W. Chao, *Permutation-invariant constant-excitation quantum codes for amplitude damping*, arXiv:1809.09801, https://eprints.whiterose.ac.uk/152034/8/1809.09801.pdf.
4. C. Cafaro, P. van Loock, *Approximate quantum error correction for generalized amplitude-damping errors*, Phys. Rev. A 89, 022316 (2014), https://doi.org/10.1103/PhysRevA.89.022316; arXiv:1308.4582.
