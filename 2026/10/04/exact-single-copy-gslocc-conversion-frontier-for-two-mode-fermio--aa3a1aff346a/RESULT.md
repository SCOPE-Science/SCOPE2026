# Exact single-copy GSLOCC conversion frontier for two-mode fermionic Gaussian entanglement
## Finding
For two single-mode fermionic parties, consider the even-parity pure Gaussian family
\\[
|\\psi_\\theta\\rangle=\\cos\\theta\\,|00\\rangle+\\sin\\theta\\,|11\\rangle,
\\qquad 0<\\theta\\le \\pi/4.
\\]
Define \\(P_G(\\theta\\to\\phi)\\) as the supremum of the total success probability over finite-round fine-grained Gaussian stochastic LOCC protocols whose terminal transcripts have product single-mode fermionic Gaussian Kraus operators, with branch-dependent Gaussian local-unitary corrections allowed. Then for every \\(0<\\theta,\\phi\\le\\pi/4\\),
\\[
P_G(\\theta\\to\\phi)=
\\min\\left\\{
\\frac{\\cos^2\\theta}{\\cos^2\\phi},
\\frac{\\sin^2\\theta}{\\sin^2\\phi}
\\right\\}.
\\]
Equivalently,
\\[
P_G(\\theta\\to\\phi)=
\\begin{{cases}}
\\sin^2\\theta/\\sin^2\\phi,&\\theta\\le\\phi,\\\\
\\cos^2\\theta/\\cos^2\\phi,&\\theta\\ge\\phi.
\\end{{cases}}
\\]
Thus Gaussian stochastic LOCC loses no success probability for concentration, but it has a strict probability penalty for dilution. In particular, the Bell-state endpoint \\(\\phi=\\pi/4\\) has optimal probability \\(2\\sin^2\\theta\\).

## Assumptions and scope
The parties each control one fermionic mode. The protocol class is the standard fine-grained pure-state GSLOCC setting: after resolving all classical transcripts, a terminal branch is represented by one product Kraus operator \\(A_j\\otimes B_j\\), with each local factor a single-mode fermionic Gaussian filter of definite fermionic parity. Branch-dependent Gaussian local unitaries may be composed into the terminal branch. The terminal Kraus family obeys the usual completeness identity. The claim concerns exact conversion of one pure state to another, not approximate conversion, catalytic conversion, many-copy rates, or arbitrary mixed Gaussian instruments with unresolved Kraus structure.

The generalized local Gaussian convention is the one used in the cited fermionic-Gaussian literature, in which parity-changing Gaussian branches and their particle-hole conjugates are admitted. Under this convention a successful odd-odd branch can be followed by local Gaussian parity flips, turning it into an even-even diagonal branch without changing its branch probability or its contribution to the completeness relation.

## Proof
First consider \\(\\theta\\le\\phi\\). The 2026 source exhibits, for every \\(0<t\\le1\\), the local fermionic Gaussian measurement branch
\\[
K_t=t|0\\rangle\\langle0|+|1\\rangle\\langle1|
\\]
with a Gaussian complementary branch. Set
\\[
t=\\frac{\\tan\\theta}{\\tan\\phi}.
\\]
Then
\\[
(K_t\\otimes I)|\\psi_\\theta\\rangle
=t\\cos\\theta|00\\rangle+\\sin\\theta|11\\rangle
=\\sqrt{p}\,|\\psi_\\phi\\rangle,
\\]
where
\\[
p=\\frac{\\sin^2\\theta}{\\sin^2\\phi}.
\\]
This proves achievability in the concentration regime.

For \\(\\theta\\ge\\phi\\), use the particle-hole conjugate Gaussian branch
\\[
\\widetilde K_t=|0\\rangle\\langle0|+t|1\\rangle\\langle1|,
\\qquad t=\\frac{\\tan\\phi}{\\tan\\theta}.
\\]
It is the local particle-hole conjugate of the preceding Gaussian filter; its complementary branch is conjugated in the same way. Directly,
\\[
(\\widetilde K_t\\otimes I)|\\psi_\\theta\\rangle
=\\cos\\theta|00\\rangle+t\\sin\\theta|11\\rangle
=\\sqrt{p}\,|\\psi_\\phi\\rangle,
\\]
with
\\[
p=\\frac{\\cos^2\\theta}{\\cos^2\\phi}.
\\]
This proves achievability in the dilution regime.

For the upper bound, fine-grain an arbitrary finite-round protocol to its terminal product Kraus operators. On every successful branch, absorb the branch-dependent Gaussian local-unitary correction into the local Kraus factors. A single-mode parity-definite local operator is diagonal if even and anti-diagonal if odd. Since a successful branch must end at the even target, its two local parities agree; if both are odd, compose local Gaussian particle-hole flips on the left. These unitary corrections preserve \\(A_j^\\dagger A_j\\) and \\(B_j^\\dagger B_j\\), so they do not alter completeness. Hence every successful branch may be written with diagonal factors
\\[
A_j=\\operatorname{{diag}}(a_{0j},a_{1j}),
\\qquad
B_j=\\operatorname{{diag}}(b_{0j},b_{1j}).
\\]
If its success probability is \\(p_j\\), exact conversion gives
\\[
\\cos\\theta\,a_{0j}b_{0j}=\\sqrt{{p_j}}\,e^{{i\\alpha_j}}\\cos\\phi,
\\qquad
\\sin\\theta\,a_{1j}b_{1j}=\\sqrt{{p_j}}\,e^{{i\\beta_j}}\\sin\\phi.
\\]
Therefore
\\[
p_j\\cos^2\\phi=\\cos^2\\theta\,|a_{0j}b_{0j}|^2,
\\qquad
p_j\\sin^2\\phi=\\sin^2\\theta\,|a_{1j}b_{1j}|^2.
\\]
Let \\(S\\) be the set of successful terminal branches and \\(P=\\sum_{{j\\in S}}p_j\\). Taking the \\(|00\\rangle\\) and \\(|11\\rangle\\) diagonal matrix elements of the terminal completeness identity gives, after discarding nonnegative failure contributions,
\\[
\\sum_{{j\\in S}}|a_{0j}b_{0j}|^2\\le1,
\\qquad
\\sum_{{j\\in S}}|a_{1j}b_{1j}|^2\\le1.
\\]
Summing the branch identities yields
\\[
P\\cos^2\\phi\\le\\cos^2\\theta,
\\qquad
P\\sin^2\\phi\\le\\sin^2\\theta.
\\]
Thus
\\[
P\\le\\min\\left\\{
\\frac{\\cos^2\\theta}{\\cos^2\\phi},
\\frac{\\sin^2\\theta}{\\sin^2\\phi}
\\right\\},
\\]
which matches the explicit filters and proves the formula.

For comparison, Vidal's unrestricted-LOCC theorem gives, for the same ordered Schmidt coefficients,
\\[
P_{{\\mathrm{{LOCC}}}}(\\theta\\to\\phi)
=\\min\\left\\{1,\\frac{\\sin^2\\theta}{\\sin^2\\phi}\\right\\}.
\\]
Consequently GSLOCC is globally optimal for \\(\\theta\\le\\phi\\), whereas for \\(\\theta>\\phi\\) unrestricted LOCC has probability one and GSLOCC has the strict value \\(\\cos^2\\theta/\\cos^2\\phi<1\\).

## Verification
The proof is symbolic and does not rely on finite enumeration. The two achievability filters can be checked by direct multiplication, and their success probabilities are the squared norms of the unnormalized outputs. The upper bound uses only terminal-Kraus completeness after branch corrections and the two exact coefficient equations forced by pure-state conversion.

The nonstandard external premise needed for achievability is that the one-mode filters \\(K_t\\) and their complementary branches are fermionic Gaussian. This is established explicitly in Appendix D.1 of Tang et al. for \\(K_t\\); the dilution filter is its particle-hole conjugate. The older Spee--Schwaiger--Giedke--Kraus paper supplies the pure-state Gaussian-SLOCC framework and the two-mode normal form.

Boundary checks are consistent: \\(\\theta=\\phi\\) gives probability one; \\(\\phi=\\pi/4\\) gives \\(2\\sin^2\\theta\\), exactly the 2026 Bell-distillation success probability; and the formula stays in \\((0,1]\\) throughout \\(0<\\theta,\\phi\\le\\pi/4\\).

## Relationship to prior work
Tang et al. (2026) prove that a local Gaussian measurement can distill \\( |\\psi_\\theta\\rangle \\) to the maximally entangled two-mode state with success probability \\(2\\sin^2\\theta\\). Their stated result is the Bell target and does not give an arbitrary-target conversion frontier or an optimality theorem for that success probability.

Spee, Schwaiger, Giedke, and Kraus (2018; first posted 2017) classify pure fermionic Gaussian states under Gaussian stochastic LOCC and show that nontrivial deterministic Gaussian LOCC transformations between fully entangled pure Gaussian states do not occur. Their classification establishes convertibility classes but does not state the exact success probability above.

Vidal (1999) gives the unrestricted-LOCC optimal probability between arbitrary bipartite pure states. Applied here it proves that the concentration half of the Gaussian frontier is already globally optimal, while also exposing the Gaussian-specific dilution gap: unrestricted LOCC is deterministic there, but fine-grained GSLOCC is not.

Targeted searches for the exact two-mode fermionic Gaussian conversion probability, the Bell endpoint's optimality, and the dilution probability did not locate a published published-finding corpus finding or primary paper stating this formula. The closest literature covers either GSLOCC class membership, deterministic impossibility, or the single Bell-distillation endpoint.

## Limitations
The theorem is deliberately restricted to exact one-copy conversion in the fine-grained single-Kraus GSLOCC model described above. It does not claim optimality over every possible unresolved multi-Kraus fermionic Gaussian instrument, catalytic protocols, asymptotic many-copy protocols, or approximate conversions. Different conventions on whether local parity-changing Gaussian corrections are free should be translated before applying the formula; the proof uses the generalized fermionic-Gaussian convention of the cited sources.

A residual literature risk remains that an equivalent success-probability formula may have appeared in older resource-theory work or a thesis under different terminology. The inspected primary sources and targeted searches did not reveal such a statement.

## References
1. Y. Tang, I. Roth, P. Faist, Z.-W. Liu, J. Eisert, and Z. Liu, “Fermionic quantum error correction is never free,” arXiv:2609.15059v1 (first public 2026-09-14), especially Theorem 3 and Appendix D.1.
2. C. Spee, K. Schwaiger, G. Giedke, and B. Kraus, “Mode-entanglement of Gaussian fermionic states,” arXiv:1712.07560v1; Phys. Rev. A 97, 042325 (2018).
3. G. Vidal, “Entanglement of pure states for a single copy,” arXiv:quant-ph/9902033v2; Phys. Rev. Lett. 83, 1046 (1999).
