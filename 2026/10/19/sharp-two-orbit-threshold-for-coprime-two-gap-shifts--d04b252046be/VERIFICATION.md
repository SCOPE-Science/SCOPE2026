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

Choosing a marked one identifies gap words up to rotation; any shorter physical period preserves the ones and makes the word a proper power. Pure words contribute only at a and b. Möbius inversion of ordered words with fixed content and division by the free rotation-orbit size gives the necklace formula. For r,s>0 the two-run word A^rB^s is primitive; for r,s≥2 the four-run word A^(r−1)BAB^(s−1) is inequivalent and could only be imprimitive by squaring, which requires r=s=2. For an independent check of coverage beyond M, choose s∈[1,a] in the residue class bs≡n mod a. Since n>(a+1)b, the resulting r=(n−bs)/a is at least two. If s≥2, the four-run lemma applies since n>2(a+b) excludes (2,2). If s=1, then r>b and a second mixed content is (r−b,1+a), making two primitive two-run words of different content. At M=(a+1)b, the only nonnegative contents are (b,1) and (0,a+1); only the first is primitive, uniquely up to rotation. The alternative bound is strictly larger iff (a−1)(b−2)<2, possible only for (2,3). At 10 there the pure (5,0) word is a power; of the two cyclic patterns with content (2,2) only the two-run one is primitive. Four endpoint/next-period examples were independently spot-checked via content counts. The universal conclusion follows from the residue argument, not these examples or the author's reported finite runs.

## originality

PASS

The supported distinct statement is the closed last-two-orbit obstruction for every coprime ordered pair of return lengths, including the exceptional pair and the sharp singleton count at the endpoint. The inspected prior literature supplies the least-period support and coefficientwise orbit counts, not this uniform cutoff. The proof uses primitive-content multiplicity and a sharp endpoint distinction beyond those known tools. This is a bounded, best-of-knowledge comparison, not a historical priority determination.

## value

PASS

Two coprime return lengths are a natural elementary mixing gap system. Two distinct primitive orbits is the first multiplicity question beyond least-period existence. The closed worst exception, including why (2,3) behaves differently, replaces arbitrary testing and gives an exact periodic-count benchmark for comparing this family with other shifts. The finding does not claim a general embedding or characterize smaller-period counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
