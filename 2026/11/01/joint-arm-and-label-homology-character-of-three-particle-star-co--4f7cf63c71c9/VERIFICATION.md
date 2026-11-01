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

# Reproduction and scope

Run `python verify.py` using Python 3.10 or newer; no third-party packages are needed. The program constructs the actual ordered Abrams cubical complex on a star with each arm subdivided into three edges. Its vertex and edge atoms are supplied with their closed supports, and its product cubes are precisely the ordered triples of atoms having pairwise disjoint supports.

It independently computes the alternating sum of cellular dimensions, compares the result to \(-m(m+1)(2m-5)\), and checks that every vertex of each tested cubical model lies in the connected one-skeleton. For the dimensions of the fixed cellular traces, it computes the action on closed supports directly and uses the permutation parity induced on the subset of moving (edge) particle coordinates. This checks orientation signs, including transpositions of moving cube factors.

The complete finite test set consists of all conjugacy-class representatives of the arm groups on three, four and five arms, paired with all three conjugacy-class representatives of the label group. There are \(9+15+21=45\) traces. The output file `verification_output.txt` is the recorded result of this execution and can be regenerated.

The checks are finite, and do not themselves prove an infinite-family theorem or independently certify publication priority. The proof for arbitrary arm number is the uniform fixed-set analysis, the coefficient identity, and the existing one-dimensional deformation theorem in `RESULT.md`. No independent audit has been performed.
