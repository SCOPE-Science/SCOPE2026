---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For H(d,q), q≥3,d≥3, two distinct sinks a,b at strictly positive rates and uniform J>0, the adjacency A has spectral levels k=0..d with eigenvalues (q−1)d−qk. The dissipative effective H=JA−iγa|a⟩⟨a|−iγb|b⟩⟨b| decays on B=⊕_k span{E_k a,E_k b} and remains norm-preserving on its orthogonal dark complement; all eigenvalues in B have negative imaginary part. At k=0 rank 1, at every k≥1 rank2 follows from two distinct Fourier phases on differing coordinate (q≥3), hence dimB=2d+1, average η=(2d+1)/q^d independent of placement. Hamming Krawtchouk Gram kernels <x,E_k y>=q^-d K_k(distance) yield exact site η(x) formula with denominators m_k²−K_k(t)²>0. Degree-one centered local tensors plus degree-two cross terms exclude all perfect-capture sites except a,b, including q=3 all-coordinates-distinct exceptional candidate. Independent exact eigenpolynomial projectors H(3,3) tested t=1,2,3, all 81 sites and ranks=7, avg 7/27, x=(2,0,0) formulas 11/27 and 71/315. Finite d=3 tests cannot establish arbitrary q,d; proof is spectral algebra.

## originality

PASS

Godsil 2010 supplies general spectral-support/controllability machinery, Varbanov–Krovi–Brun 2008 analyzes measurement-based quantum hitting and symmetry, and Razzoli–Paris–Bordone 2021 supplies one-sink irreversible capture efficiency. These are prior general/thematic ingredients, not distinct claimed inventions. The actual theorem counts two independent irreversible sinks on all H(d,q), q≥3 arbitrary separation and supplies site-resolved Krawtchouk geometry with exactly two sure-capture sites. The accessible Godsil and Varbanov full PDFs do not state this evaluated two-sink result. The full 2021 transport article was not independently read; older multiple-trap association-scheme coverage is a priority risk.

## value

PASS

The rank of an absorbing/dark subspace and capture probability are natural coherent-transport observables, and sink separation surprisingly leaves the averaged efficiency invariant despite affecting individual sites. Exact general two-sink dimension and sitewise Krawtchouk law are meaningful structural improvements beyond one-sink formulas, with clear limits for binary/disordered cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
