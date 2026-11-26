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

In the accepting-probability coordinate each transition is a strictly decreasing affine map. Thus M(n+1)=F(m(n)) and m(n+1)=G(M(n)) for the upper and lower envelopes F,G, respectively. The increasing two-step maps preserve the first forward comparison, so each extremum is monotone along each parity. Every pairwise affine comparison then has an eventually constant sign, including ties. The wording that a sign changes at most once should allow a finite intervening zero block (negative, zero, positive); this does not affect stabilization. Strict decrease gives exactly the extremizing prefix/last-letter decompositions; the number of winners cannot decrease after two steps. If uniqueness persists on a parity, the relevant optimizing and minimizing letters stabilize, and the unique word appends the same length-two block at each step. The letters of that block need not be different. For a unique final winner every prefix must uniquely attain the extremum selected by its suffix sign. If a letter were to return on a positional parity, its strict affine advantage over the intervening winner at both outer inputs would persist at the intervening monotone input, a contradiction. Counting ordered distinct run letters and positive lengths gives the stated product, with the empty subsequence counted once. Duplicate maps, arbitrary initial probabilities and determinant -1 cause no difficulty. An independently written exact integer replay checked 864 ternary grid instances through length five and the 27-word example, including the winning score and runner-up gap. The frozen output's 190 models are mixed (50 binary, 90 ternary, 50 quaternary), not all ternary as the prose says. Neither finite check proves eventual regularity.

## originality

PASS

The supported distinct contribution is the fixed-automaton two-ray theorem over arbitrary finite alphabets in the strictly negative determinant regime. Credit Gill for binary regularity and binary eventual-pattern classifications, and credit the distinct indexed parity-run finding for equivalent parity-run and product-bound content for q≥3. Those individual conclusions are not supported as distinct from that indexed finding, and repository path dates do not establish priority. Neither close comparison supplies the fixed-automaton two-ray theorem for q≥3.

## value

PASS

The surviving infinite-language result sharpens a known binary regularity question in a genuinely larger alphabet regime: for a fixed automaton the possible eventual languages have at most one specified period-two suffix ray on each parity, or uniqueness fails there. This gives more than an existence result or a polynomial list of possible words, and the exact ternary example verifies a winner using three symbols. It is useful as a structural classification under the uniform sign assumption, not a classification of mixed-sign automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
