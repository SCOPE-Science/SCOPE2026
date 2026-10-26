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

`verify_latin_rank4.py` checks actual row/column/symbol ternary incidences in cyclic addition tables of orders one through six and in the Klein-four table. It enumerates quantifier-free types of ordered prefixes up to three elements and every possible one-element extension type, including repeated elements. Order-four and order-five reduced Latin squares are exhaustively enumerated (four and 56, respectively), and their extension-type dictionaries are compared. The program checks a three-symbol \(2\times2\) rectangle exists in the cyclic-four square but not in the Klein-four square. Its included output ends in `VERIFY_OK`.

The symbolic extension lemma in RESULT.md—not this finite program—proves the rank-four statement for every finite Latin square of order at least four. The distinct-order lower bound uses sentences demanding two, three, or four distinct rows. The rank-five witness is a sentence with four nested row/column quantifiers and two sibling fifth-level symbol quantifiers; this is a rank-five sentence even though it contains six quantifier occurrences.

Reproduce by running `python3 verify_latin_rank4.py` in the package directory. No external packages are required.
