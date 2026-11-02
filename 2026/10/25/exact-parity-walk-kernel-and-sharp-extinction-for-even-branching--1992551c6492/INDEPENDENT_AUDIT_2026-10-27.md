# Independent mathematical audit

## correctness

PASS

Independently verified the exact resolvent column g_u=z^(d(u,v)) S_(depth LCA(u,v)) where S_r=sum_(s=0)^r z^(2s) in F2[z]. For u off the root-to-v path, parent relation g_u=z g_parent and even child count cancel; for proper ancestors of v the toward-v child and an odd number of off-path children cancel using S_r+z^2 S_(r-1)=1; at u=v the same identity yields 1. Thus (I+zA)g=e_v and all walk parities follow for every finite permitted tree and every time. Top degree i+j<=2h gives A^(2h)=ell ell^T nonzero and A^(2h+1)=0, including h=0; exactly half of states have deepest-layer parity 1. An independently constructed irregular 11-vertex even-child tree verified the whole matrix-power kernel and nilpotent cutoff, not used as infinite proof.

## originality

PASS

Ceccherini-Silberstein et al arXiv:1205.6785 study automata on infinite regular rooted trees and associated shift properties. Akın/Cayley tree papers focus on entropy/reversibility. A general GF2 adjacency power equals walk-parity fact is elementary but does not itself supply the depth-LCA closed formula or arbitrary even-child extinction theorem. Resultary related entries concern modular Laplacian or complete-multipartite parity automata on different graph families; no implication established. Older binary-tree spectral/walk formulas remain a bounded risk.

## value

PASS

The full time-and-pair walk-parity kernel is a structural invariant on an unrestricted class of finite rooted trees whose nonleaf branching can vary arbitrarily among positive even values. Branch multiplicity disappears from the formula, and the exact sharp extinction time and half-state last step are novel motivated propagation features useful for finite-field graph dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
