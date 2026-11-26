# Independent mathematical audit

## correctness

PASS

For a fixed finite graph and γ>0, energy pinching is the large-time channel; the limits of the uninserted and inserted site distributions are Fe_v and F²e_v, respectively, when both time intervals tend to infinity. Channel convergence is uniform away from the two endpoints for any fixed accuracy, and excluded endpoint intervals have vanishing relative length. This verifies the half-L1 residual and order of limits. The distinct eigenspaces at 0 and m+n are rank one; the zero-sum sectors inside each part have eigenvalues n and m and are omitted if empty. For m=n the correct projector merges the two zero-sum blocks; their disjoint supports make the entrywise-square formula unchanged. With N=m+n, F has eigenvalues 1 on constants, 1−2/N on the part-contrast vector, and 1−2/m or 1−2/n on the corresponding within-part zero-sum sectors. In (F−F²)e_v, the within-initial-part coefficient A=2(m−2)/m² vanishes at m=2 and the mode is absent at m=1. The contrast coefficient is B=2(N−2)/N², including zero at N=2. For m≥3 the check Bn/N<2n/N²≤1/(2m)<A shows that only v has positive mass; since the vector has zero sum the residual is exactly that mass. For m≤2 its positive mass is Bn/N, zero in the trivial K₁,₁ case. This gives both formulas. The positive correction for m≥3 is bounded by 2/(mN). The limiting expression increases until 3+√3 and decreases thereafter, so only integers 4 and 5 can maximize it; g(4)=3/16<24/125=g(5), completing the discrete comparison omitted in the proof's last sentence. Independent numerical eigenspace grouping evaluated 12 graphs, including balanced, unequal, singleton, and m≥3 cases, agreeing within 2×10⁻¹². Replay: /workspace/branches/dad7f9af-618f-46cd-947b-ad1e61410056/check_residual.py. Uploaded verification was inspected, not run. The finite test supplements the algebra and does not test a uniform relaxation time.

## originality

PASS

The general two-time reduction and the P₃ example are covered by prior work and credited by the frozen record. The supported distinct claim is the exact arbitrary-rectangular Laplacian residual, including its sign split and fixed-shore threshold and maximum. The strongest inspected mixing and intrinsic-dephasing results do not establish that evaluated residual or its consequences. This is a bounded best-of-knowledge conclusion.

## value

PASS

For a standard quantum-walk temporal consistency test, a natural graph expansion can leave a strictly positive long-time signal. The exact threshold separates initial shores with no surviving signal from those whose within-part zero-sum mode contributes at order one; the finite correction and unique optimizer quantify the effect. This is not mere recomputation of a trace or a small-table entry, and it requires only the stated ordered limits, not uniform-in-size dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
