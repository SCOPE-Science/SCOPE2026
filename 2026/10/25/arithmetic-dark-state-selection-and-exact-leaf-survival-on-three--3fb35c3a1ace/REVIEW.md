# Scientific assessment

## Correctness

**PASS.** The nondecaying subspace of \(H-i\gamma|o\rangle\langle o|\) is precisely the span of adjacency eigenvectors vanishing at the hub. Any real eigenvalue has a hub-zero eigenvector by the imaginary-part identity, and finite-dimensional contractivity excludes a Jordan block on the real axis. The complement decays. Dirichlet path modes are normalized sines, and a common eigenvalue across \(k\) arms yields \(k-1\) hub-zero modes. The leaf projection uses a one-dimensional normal vector with weights proportional to \(1/\sqrt{L_i+1}\); summing \(\sin^2\) across common angles proves the claimed gcd formula. Numerical full-matrix, exact rational Krylov-rank, and dissipative spectral checks all passed. The all-length proof is analytical; finite checks are not substituted for proof.

## Originality

**PASS against the inspected evidence, with material residual uncertainty.** The 2006 Konno study concerns homogeneous-tree unitary quantum walks, not absorption on arbitrary three-arm spiders. The direct 2018 Yalouz–Pouthier star-trapping study describes equal-length branches; however, its full text could not be inspected, so the abstract cannot exclude every possible broader result. The accessible 2022 follow-up by the same authors explicitly imposes the equal-branch-length architecture and investigates peripheral defects and optimal trapping speeds. The 2021 Razzoli–Paris–Bordone paper provides the general spectral projection method and treats several different graph families, but not the stated explicit gcd collision classification and rational leaf survival across arbitrary three unequal lengths. Relevant published-record searches encountered spider geometry and spectral partition results without the claimed absorption observable. The equilateral special case is understood as background, not as separately original. An unlocated general Jacobi or spectral observability result could still subsume portions of the theorem; exhaustive priority is not claimed.

## Mathematical value

**PASS.** The arithmetic collision of Dirichlet spectra turns physical arm-length choices into a complete yes/no law for absorption from a specific leaf. The theorem also computes the full dark dimension and the exact nonzero survival, including the distinction between graph-wide dark modes and modes accessible from the chosen starting leaf. For instance, lengths \((4,5,11)\) support five protected modes although the first leaf is completely absorbed. This exact infinite-family classification is more informative than a few finite examples or a generic algorithm for matrix projection. It can guide finite excitonic tree geometry without suggesting unproved perturbation robustness.

## Sources and residual risks

Primary texts materially read: N. Konno, arXiv:quant-ph/0602213 (abstract, finite-tree model, quantum-walk definitions and conclusions); S. Yalouz and V. Pouthier, arXiv:2210.17524 (introduction, equal-arm graph definition, rotational block reduction and dynamics); L. Razzoli, M. G. A. Paris and P. Bordone, *Entropy* 23, 85 (2021) (spectral projection method, graph families, summary and appendix). S. Yalouz and V. Pouthier, *Physical Review E* 97, 022304 (2018), was available only as an abstract; it is a genuine historical-priority risk and was not treated as whole-document evidence of absence. Earlier starlike-tree spectral classifications and broader observability results may contain a stronger implication that these searches did not settle.

Finite verification limits: the standalone script checks 492 short-length combinations numerically, 24 configurations by exact integer Krylov rank, and 21 lossy-generator eigenvalue cases. These do not exhaust infinite arm lengths. No assertion is made about the detailed absorption-time law, disorder, other trap configurations, or independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
