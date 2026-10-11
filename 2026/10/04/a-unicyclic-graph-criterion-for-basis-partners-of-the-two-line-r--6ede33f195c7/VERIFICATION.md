---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Vanishing of a coefficient vector on the full vertical line is equivalent, by the \(p\)-point Fourier transform, to zero left-vertex edge sums; vanishing on the diagonal similarly gives zero right-vertex sums; the extra point adds the weighted functional \(\psi_B\). Thus the kernel is exactly the unsigned incidence kernel intersected with one hyperplane. The incidence rank of a bipartite graph is \(n_B-c_B\), giving \(\beta_B=2p-n_B+c_B\) and the stated nullity drop by at most one. Invertibility forces \(\beta_B=1\), hence a spanning connected graph with \(2p\) vertices and edges, i.e. unicyclic. Its incidence kernel alternates on the unique even cycle, so the extra functional is \(S_C\). For prime \(p\), if the alternating label polynomial of degree at most \(p-1\) vanishes at a primitive \(p\)th root and at \(1\), cyclotomic divisibility forces all label-count differences to vanish, proving the multiset criterion. The reduced-incidence Laplace expansion yields the determinant after the two inverse Fourier row transforms. Independently, exhaustive \(p=3\) enumeration of all \(\binom96=84\) candidates found 75 invertible matrices and exactly the same 75 graph-criterion candidates, with zero mismatches.

## originality

PASS

The Ferguson--Mayeli--Sothanaphan full text introduces exactly this family in Question 1.10 and asks about its Riesz-ratio asymptotics, but does not give a graph/unicyclic classification of basis partners. Its general determinant and basis-pair definitions do not imply the incidence reduction. Resultary searches found other quantitative-spectrality findings for different families, but no earlier theorem with this graph criterion or cycle determinant formula.

## value

PASS

The theorem gives a complete structural classification of all basis partners for the exact family singled out by an open quantitative-spectrality question, together with a determinant formula and general nullity law. Even without solving the final Riesz-ratio asymptotics, this sharply reduces the surviving search space to labeled unicyclic graphs and supplies a natural invariant needed for further work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
