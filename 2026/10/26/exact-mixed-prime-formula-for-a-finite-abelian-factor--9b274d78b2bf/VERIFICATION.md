---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Every irreducible of the product has the form rho tensor lambda with lambda linear. If rho(g)lambda(a)=I, the common inverse scalar has both p-power and q-power order, hence is 1. Thus the individual kernels split, and a faithful sum must separately separate both factors. A nontrivial normal subgroup of P meets Z(P), by the P-conjugation class equation on that subgroup. By Schur, the restrictions of irreducibles to the center are scalars given by central characters. The central characters in a faithful sum generate the dual center. Reduce them modulo p in that finite abelian p-group and select a basis from their images; the selected s=d(Z(P)) characters still generate the dual (a finite p-group quotient equal to its p-multiples is zero). Thus any faithful sum for P contains a faithful s-constituent subsum, and any minimum-degree one has exactly s constituents. A faithful sum for P times A has m>=r=d(A) constituents and contains s whose P-parts cost at least delta(P). All other constituents cost at least one. Attach distinct positions of a generating list for the dual of A to the s optimal P-constituents, and supply any additional needed generators in one-dimensional constituents with trivial P-part. This attains precisely the lower bound, including r=0 and r=s. Finally delta(A)=r by the generator criterion for its linear characters, giving the stated equivalent saving.

## originality

PASS

The closest direct product paper gives same-prime additivity and two exact mixed-prime examples covered here. The inspected central-character results provide the optimal constituent count for the p-factor and the generator count for the abelian factor, but do not give a minimum for their coprime product. The supported distinct claim is the exact general rank correction: the p-factor's necessary faithful subsum costs delta(P), and each abelian generator beyond its available constituent count costs exactly one. This fills the exact mixed-prime case rather than claiming novelty for the central-character facts or the examples.

## value

PASS

The formula gives the exact attainable saving for a natural first nonadditive direct-product problem, uniformly across arbitrary p-groups and abelian q-groups rather than only cyclic or low-order examples. It explains why the saving uses the number of necessary constituents and not the dimension of their direct sum; in particular it separates the regime of no added dimension from the regime of one unit per excess generator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
