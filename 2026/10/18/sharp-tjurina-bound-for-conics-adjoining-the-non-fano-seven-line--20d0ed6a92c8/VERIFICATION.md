---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

A seven-line arrangement with exactly six ordinary triples and three nodes is projectively the non-Fano configuration: writing r(L) for original triple incidences gives each line r=2 or3, four high lines with r=3 and three low lines with r=2. Counting original triples by high-line multiplicity shows each of the six pairwise high-line crossings is a different triple completed by a low line, and the low lines implement the three perfect matchings, yielding the displayed normal form. For an allowed smooth conic Q the six old triples are avoided; h in {0,1,2,3} is the number of old double points on Q, and t the number of conic-line tacnodes. Bézout gives n3=6+h, 35=n2+2t+3n3, and tau=n2+3t+4n3=41+h+t. Every five-line subset contains a triple concurrent triple, and three concurrent lines cannot all be tangent to a smooth conic, hence t<=4. For h<=1 obtain tau<=46. For h=2, all low lines pass through at least one selected old double so none can be tangent; a hypothetical t=4 forces all four high lines tangent. Their invertible dual conic matrix has diagonal zero, off-diagonal u,v,w≠0, u+v+w=0; evaluating the primal adjugate at the three old double points yields 4uv,4uw,4vw≠0, contradicting h=2. For h=3, none of the low lines tangent, and any conic passing through all three old doubles has Q=a x²+b y²+c z²+(a+b+c)(xy+xz+yz). The four high-line tangency discriminants exclude every triple of tangent high lines: first three imply impossible a=b=c with 9a²=4a², while two coordinate axes plus diagonal force c²+4r²=0 and c(c-4r)=0, hence r=c=0 in characteristic zero. Thus h=3 has t<=2. The bound h+t<=5 is universal within the stipulated configuration. For the explicit Q=(x-y)²-4i(x+y)z-4z², my independently evaluated symmetric quadratic matrix has determinant16 and the dual tangency values [0,0,0,-16,8i,8i,-16+16i]; it passes through exactly two old doubles, none of the six triples, with three separate tacnodes at the listed points, giving n2=5,t=3,n3=8 and tau=46. The nearly-free degree-nine formula tau=(r-4)²+47>=47 excludes nearly freeness for this *stratum* and does not claim a general degree-nine result. These arguments reconstruct the full infinite complex-conic case; numerical tests do not replace the algebraic exclusions.

## originality

PASS

Best-of-knowledge original sharp 46 Tjurina ceiling for the entire *six-triple-point non-Fano seven-line plus smooth conic* stratum and the resulting specific degree-nine nearly-free exclusion. Dimca–Pokora (2022) Proposition5.6 forbids *free* arrangements of seven lines plus conics and shows a related extreme obstruction, but its printed inequalities and case analysis do not provide the present sharp maximal tau or the distinct near-free boundary tau>=47. Gałecka (2022) explicitly leaves degrees 8 and 9 nearly-free existence unresolved in general. The statement is not broadened to all degree-nine line/conic arrangements; the new bound supplies exactly the additional obstruction for a geometrically canonical stratum.

## value

PASS

The non-Fano seven-line core is the uniquely extremal six-original-triple stratum singled out by prior attempts to rule out free conic extensions. Determining its *sharp* allowed Tjurina number with an explicit complex smooth conic witness is a motivated exact structural bound. Excluding the narrowly unresolved degree-nine nearly-free boundary tau>=47 for this stratum advances a recognized classification problem, without pretending to solve the entire degree-nine case. The result relies on dual-conic geometric restrictions, not mere substitution into a known formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
