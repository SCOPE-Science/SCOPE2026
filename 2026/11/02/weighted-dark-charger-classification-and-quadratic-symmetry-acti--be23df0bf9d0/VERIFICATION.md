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

In battery-last notation, the exchange term sends |00,1> into (g1|10,0>+g2|01,0>) and |11,0> into (g2|10,1>+g1|01,1>). Both two-level bright blocks have detuning magnitude |Delta| and coupling G, so the population swap is q. For an excited input the two possible leakage channels land in orthogonal charger excitation sectors; their total q(|a00|^2+|<Bdown|zeta>|^2) vanishes exactly on span{|11>,D}. The excited-output vectors from battery inputs |0> and |1> lie in orthogonal charger subspaces, so the pumping law holds for coherent and mixed inputs. The squared overlap of D with Bup is ((g1^2-g2^2)/G^2)^2=1-C_D^2. The two-qubit determinant formula gives C=c C_D and hence the claimed affine law. For readout, the difference between normalized conditional charger marginals is traceless. Choose the first spin axis perpendicular to its first Bloch vector; choose the second perpendicular to both the second Bloch vector and the contracted correlation matrix. Each of the four product projectors then has identical probabilities on the two marginals, so conditioning on a nonzero-probability outcome preserves the same energy expectation. Adaptive repetition gives the scalar geometric law without suppressing battery shot noise. The quadratic asymptotic is about an admissible symmetric reference q(0)>0: at fixed g, detuning and pulse duration, q is even in epsilon, giving r=4q(0)epsilon^2+O(epsilon^4). D is the weighted family D(epsilon), not the unchanged symmetric singlet. A stroboscopically frozen reference q(0)=0 lies outside this asymptotic claim. Direct Taylor evolution of a resonant three-qubit example with g1=2, g2=1, c=1/2, e=1/3 and q=1/2 gives 0.5599999999999998, agreeing with 14/25 (node /workspace/independent_checks.js, section 3). The single numerical example is not the proof, and the uploaded verifier was inspected, not run.

## originality

PASS

The supported distinct result is the complete unequal-coupling pure full-charge-preserving family, with its weighted concurrence–charging law and symmetry activation. The symmetric exchange probability and adaptive equal-energy idea were already present. Gong et al.'s exact equal-g Hamiltonian does not contain the independent ratio g1/g2: the two bright vectors coincide there and differ in the asymmetric case, so merely substituting G for sqrt(2)g in the known pulse probability does not yield the classification or activation. The closest concurrence-frontier record explicitly excludes asymmetric couplings. Other checked near matches concern one-ancilla or dissipative models, not the exact weighted collision law. This is a bounded comparison, not a historical priority certification.

## value

PASS

Preserving full charge while pumping an incompletely charged battery is an operationally natural design constraint. The proof identifies every admissible pure charger, derives the exact entanglement–pumping tradeoff and exposes a qualitatively distinct response to imbalance through a coupling-dependent dark direction. The local readout result makes the population law apply to every allowed trajectory, not just an average, without claiming elimination of single-shot energy noise or any preparation or readout cost advantage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
