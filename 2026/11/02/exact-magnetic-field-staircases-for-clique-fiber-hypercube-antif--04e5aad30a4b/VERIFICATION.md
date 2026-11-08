---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For d>=3 the graph has vertices (i,s), i<d, s in F_2^d, with word-fibre K_d edges and layer bit-flip edges along j!=i; degree 2(d-1), N=d 2^d vertices, N(d-1) edges. For a spin-up set S of size r<=N/2, |boundary S|=2(d-1)r-2e(S) and e(S)>=sum_s binom(a_s,2). Convex exchange shows minimum for a_s=q or q+1 with q=floor(r/2^d), giving B_d(r)=2(d-1-q)r+2^d q(q+1). Assign each layer a binary parity target with nearly equal class sizes; select vertices (i,s) with parity(s)=target_i. This selects N/2 sites with no internal lateral edges and balanced occupancies; removing a site from any fullest fibre preserves properties, proving equality for every 0<=r<=N/2 without finite extrapolation. Spin inversion covers all r. Hamiltonian exchange minimum J[N(d-1)-2B_d((N-|M|)/2)] follows. Minimizing the resulting convex piecewise linear function at positive field gives exactly h_q=2J(d-1-q), 0<=q<=floor((d-1)/2), including truncated terminal sector for odd d. At d=3 the coordinate representation produces the 24-site rhombicuboctahedron, and a complete independently written 2^24-state cut count gives the exact half-sector multiplicities and coexistence totals 1392 at h=2J and 13875 at h=4J; plateau M=8 has 234. The finite census certifies only d=3 multiplicities; all-d sector maxima are analytical.

## originality

PASS

The all-dimension exact fixed-magnetization maximum cut and critical-field staircase for the specific clique-fiber Boolean-cube graphs are additional to standard Ising/max-cut conversion and convex occupancy. Primary spin-cluster papers Schmidt–Richter–Schnack 2005 and Rousochatzakis–Läuchli–Mila 2007 treat 12-site cuboctahedron and 30-site icosidodecahedron (quantum Heisenberg plus Ising-limit analyses), not the present 24-site rhombicuboctahedron and all-dimension family. Published research on the latter graph’s independence/Rips complexes concerns topology and does not imply cut counts. A broader unknown graph optimization theorem might cover this construction; the conclusion is best-knowledge qualified.

## value

PASS

The 24-vertex rhombicuboctahedral antiferromagnet is a canonical naturally frustrated finite spin cluster, and its higher-dimensional coordinate-clique family is a systematic geometrically motivated extension. All-sector exact ground energies, all critical fields and a parity-driven odd/even effect solve a complete natural optimization question over exponentially many configurations; the independent exact finite labelled-degeneracy census supports benchmarking. Not mere textbook Ising-to-cut reduction or an arbitrary small finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
