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

The proof is deductive. A separate finite replay checks the combinatorial classification without being used to infer the infinite statement.

The verifier enumerates every weak order on labeled coordinate sets of sizes \(1\) through \(6\). For each weak order it computes the complete equality pattern and every atomic value of
\[
R(x_i,x_j,x_\ell)\iff r_i<r_j\land r_i<r_\ell\land r_j
e r_\ell,
\]
then groups weak orders by the resulting quantifier-free signature.

The output is:
- complete-type counts \(1,3,13,75,541,4683\);
- quantifier-free-type counts \(1,2,7,38,271,2342\);
- exactly one signature class of size \(1\) in every arity, namely the constant tuple;
- every other signature class has size \(2\);
- on injective tuples, the counts are \(n!\) complete types and \(n!/2\) quantifier-free types for \(2\le n\le6\).

The script terminates with `VERIFY_OK`. The all-arity proof in `RESULT.md` explains why the same two-to-one classification holds for every \(n\).
