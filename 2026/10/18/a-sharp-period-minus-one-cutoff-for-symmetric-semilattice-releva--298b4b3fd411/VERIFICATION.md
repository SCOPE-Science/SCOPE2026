---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a fixed set of size a and a partner of size b, the overlap can be any integer from 0 to min(a,b), so output sizes are exactly [max(a,b),a+b]. At a fixed a, a small partner b yields those sizes directly (if a is in the tail they are a+[0,b]). A tail partner of residue r yields precisely the tail residues r+[0,a] modulo m: every union size differs from the partner size by at most a, and choosing b≥max(a,k) in residue r realizes every increment. Thus the rows of reachable pairs depend only on the current signature precisely when the least tail size k is at least m−1 (including m=1). When k<m−1, sizes k and k+m have the same signature but different rows: the tail partner of residue k can reach residue k+k+1 only from the larger set. Take p true on that partner class and q false exactly on that output class; p→q separates the two sets. More generally, any missing projected (partner,output) pair at a representative is detected with these singleton/complement valuations. This verifies the quantifier order of the bounded-morphism back condition; forth is by projection. The usual induction using both directions for implication gives preservation at every finite set, in particular the empty set. A common multiple of the atomic periods and a cutoff at least max(common preperiod,m−1) yield the exact finite procedure. This uses an infinite ground set and only signature-invariant atomic valuations. Inspected the frozen finite arithmetic checker without using its recorded output as proof.

## originality

PASS

The relevant semantics, p-morphism preservation and the infinite cardinality interval model have clear prior precedents. The supported distinct claim is the sharp finite prefix/period quotient criterion and the one-implication obstruction, not introduction of that semantics or a solution to unrestricted validity. No inspected source gives or mechanically implies the cutoff without the extra analysis of the finite modular projection.

## value

PASS

The periodic-cardinality abstraction is natural for permutation-invariant valuations, but union with overlap is not a function of the two signatures. The result gives an exact cutoff for when relational reachability nonetheless suffices for nested implication, a minimal-depth counterexample when it does not, and a concrete finite decision procedure for specified ultimately periodic atoms. This is a meaningful boundary for a standard relevant semantics, not a claim about all valuations or a mere counting formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
