---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Adjacent distinct permutation rows have at least one strict ascent; exactly one implies coordinatewise translation by -1 (mod n) from conservation of their symbol sum. A single exceptional adjacent-row boundary cannot close a Latin column, so total excess two over n-1 boundaries requires exactly two two-ascent boundaries. The intervening regions are three nonempty cyclic runs of lengths a,b,c. The binary choice of ordering the last two complementary arcs yields column-type set S in Z_n. The starts of the second and third row blocks are permutations iff S is invariant under translations by b,c, hence occupies t residue classes modulo g=gcd(a,b,c). Counting exact crossing locations gives two exceptional ascent numbers 1+t c/g and 1+t a/g. Each equals 2 only if t=1 and a=c=g; thus g|n and 3g<=n. Conversely these conditions make all rows/columns Latin and give exactly n+1 ascents; the two boundary positions, first row and S recover unique parameters. Reverse rows to obtain complementary coefficient. Independently rebuilt every family for n=3,4,5,6,8,9,12,18, with normalized counts 1,1,1,3,3,4,10,12, and separately exhaustively searched all normalized squares n=3,4,5, finding 1,1,1. These finite checks do not prove general n; the three-arc proof does.

## originality

PASS

Mirzavaziri–Yaqubi, Latin Eulerian Numbers (arXiv:2609.25100v1), already prove one-ascent rigidity, extremal support gap and symmetry, but do not classify the first non-gap unrestricted coefficient for all n. Their companion Cyclic Latin Eulerian Numbers (arXiv:2609.28808v1) Theorem 3.4 establishes only T_n^c(n+1)=n in its proper cyclic family; its Section 8 finite table gives T_6(7)=2160. The theorem here supplies n! times a divisor-dependent sum across all labeled Latin squares; for n divisible by d>=2, additional families occur and prior cyclic count cannot imply them.

## value

PASS

The first attainable coefficient after a published sharp gap is mathematically canonical. Determining it at every Latin-square order and classifying all extremizers bijectively reveals genuine divisor-dependent structure beyond the already known small tables and proper cyclic subclass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
