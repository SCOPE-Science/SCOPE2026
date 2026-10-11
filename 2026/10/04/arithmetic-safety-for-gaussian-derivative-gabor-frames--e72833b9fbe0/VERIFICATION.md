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

After dilation the window is a fixed Gaussian derivative with stable integer shifts, because the periodized squared Fourier modulus is continuous and cannot vanish at every integer translate. The non-frame criterion therefore produces a bounded-coefficient Gaussian shift-invariant entire function whose \(m\)-th derivative vanishes on the lattice. For \(N>m\), differentiating the Wronskian fewer than \(N-m\) times yields generalized row orders whose sum is too small to avoid the row order \(m\); hence each common \(m\)-th derivative zero has Wronskian multiplicity at least \(N-m\). Faulhuber--Petersen's translate-independence, automorphy, and Gaussian zero-density steps then give \((N-m)/(N\delta)\le1\). Arbitrarily large \(N\) are allowed for irrational \(\delta\), while for \(p/q\) one takes \(N=q\), yielding exactly \(q-p\le m\).

## originality

PASS

Faulhuber--Petersen determine the first-Hermite case and their primary description explicitly uses first-derivative zeros, Wronskian multiplicity \(N-1\), and the resulting rational obstruction \((q-1)/q\). Gröchenig--Romero--Stöckler treat derivative sampling and multi-window systems, but not the single-window arithmetic theorem for one lone higher Gaussian derivative. No prior \(q-p\le m\) classification was located.

## value

PASS

This is a structural extension of a newly introduced Wronskian-amplification method: it turns the exact first-derivative obstruction into an all-order irrational-safety theorem and a clean rational deficit barrier. The higher-order multiplicity lemma is independently reusable and the statement addresses a natural frame-set boundary rather than a finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
