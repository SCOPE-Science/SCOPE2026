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

The sharp lower bound is symbolic: a two-element Boolean frame has no proper nontrivial subalgebra, and a four-element Boolean algebra has only the proper Boolean subalgebra \(\{0,1\}\), whose identity and universal congruences always extend.

The explicit eight-element witness is
\[
f=(0,1,2,3,4,7,7,7).
\]
The stable subalgebra \(C=\{0,4,3,7\}\) has the congruence with classes \(\{0,4\}\) and \(\{3,7\}\). Its only possible Boolean-congruence extension to the full powerset algebra is the kernel indexed by bit \(4\), but \(1\equiv_4 5\) while \(f(1)=1\) and \(f(5)=7\) are not equivalent modulo \(4\).

The bundled `verify.c` then performs a complete independent finite replay. It checks all \(256\) unary functions on the four-element Boolean algebra, all \(16{,}777{,}216\) unary functions on the eight-element Boolean algebra, every proper Boolean subalgebra, and every compatible local and global congruence.

It also recomputes Burnside fixed-point counts under all six atom permutations, identifies all normal closure operators, and verifies the four failing closure-operator isomorphism representatives.

Expected exact output includes:

- labelled CEP failures: \(1{,}216{,}800\);
- CEP-failure isomorphism classes: \(205{,}724\);
- normal closure operators: \(45\), with \(13\) CEP failures;
- closure-operator isomorphism classes: \(14\), with \(4\) failing classes;
- `VERIFY_OK`.

## Limits

The exhaustive computation is complete only for Boolean reduct size eight. The proof of the lower threshold does not depend on computation.
