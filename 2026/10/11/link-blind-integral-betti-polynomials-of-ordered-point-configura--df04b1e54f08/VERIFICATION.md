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
# Verification of the link-blind integral Betti polynomial

The calculation is a uniform proof, not an inference from finite examples. For \(s\ge0\) added punctures, the compact Alexander-duality set in \(S^3\) is the disjoint union of the \(n\) link circles and \(s+1\) points, including infinity. Its reduced homology in degrees \(1\) and \(0\) is \(\mathbb Z^n\) and \(\mathbb Z^{n+s}\), respectively. Consequently the punctured Euclidean complement has free cohomology ranks \(1,n,n+s\) in degrees \(0,1,2\), and zero elsewhere.

Excision at the removed \(s\) ordinary points gives local relative degree-three cohomology \(\mathbb Z^s\). Since the unpunctured link complement has no degree-three cohomology, this yields a short exact split sequence of degree-two groups. A Gauss class built from the difference of two configuration coordinates restricts with degree \(+1\) on the sphere about the corresponding puncture and degree \(0\) around every other puncture. Along with the last-coordinate pullbacks of degree-one and degree-two link-complement classes, these yield an integral fiberwise basis. Leray–Hirsch therefore multiplies the cohomology Poincaré polynomial by \(1+nt+(n+k-1)t^2\) when the \(k\)-th point is added.

The base case \(k=1\) is \(1+nt+nt^2\). The product formula follows by induction for every integer \(k\ge1\), independently of link embedding. In the homotopy distinction, all pairwise diagonals in the ambient Cartesian power have codimension \(3\), so deleting them does not change \(\pi_1\). The trefoil knot group has nonabelian \(S_3\) as a quotient, whereas the unknot knot group is cyclic; their configuration spaces cannot be homotopy equivalent.

As elementary checks, for \(n=1,k=2\) the product expands to \(1+2t+4t^2+3t^3+2t^4\), and in general the degree-one and degree-two ranks are \(nk\) and \(nk+(n^2+1)\binom{k}{2}\). Such expansions are internal consistency checks, not certificates for infinitely many parameter values. There is no independent audit or assertion about cup-product rings, configuration quotients, or moving-link total spaces.
