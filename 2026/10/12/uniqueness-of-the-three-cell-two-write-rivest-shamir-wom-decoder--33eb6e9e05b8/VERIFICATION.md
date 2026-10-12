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

Run `python3 verify.py` with a standard Python 3 interpreter.

The script enumerates all \(4^8=65{,}536\) interpretation functions from the eight binary cell states to the four message labels. For each function it independently asks whether every message has a possible first-write state whose upward cone contains representatives of all four second messages.

It then verifies that the complete admissible set has size \(24\), equals exactly the set of all message relabelings of the Rivest–Shamir decoder, uses precisely \(000,001,010,100\) as the forced first-generation representatives, pairs every state with its bitwise complement, and has exactly \(16\) legal second-write transition tables on the four reachable first-generation states.

The canonical newline-terminated decoder list has SHA-256 `9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081`.

The verifier does not assign significance to update-function values on states that cannot occur after the first write; those values are outside the scientific claim.

Expected output:
`VERIFY_OK states=8 interpretations_checked=65536 admissible_decoders=24 message_relabeling_orbits=1 forced_first_states=000,001,010,100 complement_pairs=true reduced_second_write_choices_per_decoder=16 reduced_schemes=384 decoder_sha256=9afddc5cdab8eeea0ca83cf1d4d5261165fd40795d7cc7648cf413d982201081`
