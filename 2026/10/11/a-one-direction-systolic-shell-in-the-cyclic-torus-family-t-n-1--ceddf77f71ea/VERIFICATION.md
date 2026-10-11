---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof uses the standard triangular lattice with step set
\[
\pm(1,0),\quad\pm(0,1),\quad\pm(1,1).
\]
The quotient label is \(a+3b\pmod n\), so the deck lattice is
\[
L_n=\{(a,b):a+3b\equiv0\pmod n\}.
\]
The exact word norm is
\[
N(a,b)=\max(|a|,|b|,|a-b|).
\]
For \(n\ge17\), every endpoint of a path of at most four edges has \(|a+3b|\le16<n\), so a closed projected path at those lengths satisfies \(a+3b=0\) as an integer equality. Exhausting the six allowed step types shows that the first nonzero relation occurs at length four and is exactly \(\pm(-3,1)\).

For any class outside \(\mathbb Z(-3,1)\), one has \(|a+3b|\ge n\), while \(|a+3b|\le4N(a,b)\), giving the lower bound \(\lceil n/4\rceil\). The four residue-class witness vectors in `RESULT.md` attain it.

The checker also reconstructs the cyclic one-skeletons for every \(17\le n\le40\), exhausts their simple three- and four-cycles, and confirms that exactly \(n\) homologically nonzero four-cycles occur and that they are precisely the consecutive four-cycles.

Exact successful output:

`VERIFY_OK short_relation_vectors=none_through3;length4=plusminus(-3,1) | family=T_{n,1,3} range=n>=17 H1=Z^2 | simple_integral_1_systole=4 minimizers=n consecutive_4_cycles one_primitive_direction=yes | second_independent_homology_minimum=ceil(n/4) | finite_replay=n17..40 passed`
