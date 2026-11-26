# Independent mathematical audit

## correctness

PASS

With g(x)=B-max(0,mx), F^2(x,y)=(g(x),g(y)) and F^4(x,B)=(g(g(x)),B). The first three physical iterates cannot equal (B,B): respectively the second, second, and first coordinates differ from B. Writing a=(m-1)B/m^2 and b=B/m, the fourth iterate has first coordinate B for x>=b, m^2x+(1-m)B in (0,B) for a<x<b, and nonpositive first coordinate for x<=a. The latter hits (B,B) at the fifth iterate, including x=a; x=b hits at four. The interior affine map centered at c_m=B/(m+1) expands signed distance by m^2. Therefore S_n=(c_m-c_m m^(-2n),c_m+(B-c_m)m^(-2n)) is exactly the open survivor interval after n excursions, with endpoints exiting at excursion n. This proves the ceiling and the side-dependent extra iterate. The exceptional primitive period-four orbit repels along the section (the fourth map in the full plane has a locally reset transverse coordinate, so this is not a claim of two-directional plane repulsion). Each survivor length is B m^(-2n) and each escaping shell has left:right lengths 1:m, giving independence and the stated geometric law, PGF and mean. Multiplying the ceiling by m-1 suppresses its bounded error; ordinary fixed x gives the stated log limit, while the central initial point has logarithm log(2m/(m-1)), proving the separate scale. The limiting function has null level sets under any density, which justifies dominated convergence for all t>=0 and the exponential specialization. Replay: RESULT.md lines 56–82; python3 /workspace/review_evidence/bounded_checks.py tests both exact endpoints of the first eight survivor shells for m=2. The frozen verifier was read, not executed: its 5,856 total is a counter of check units, not literally 5,856 assert statements executed, and finite samples do not prove the real-parameter limits.

## originality

PASS

The map, affine section return with absorbing endpoint, four-cycles and approach to unit return slope are explicit prior results. The supported addition is the exact physical first hit of a specified cycle point including the one-iterate phase correction, and its uniform and general-density limit laws, especially the distinct deterministic midpoint scale. The strongest competing transient record concerns a later-dated full-square ensemble and entry into the cycle as a set.

## value

PASS

The physical roof resolves a meaningful phase-specific first-hitting problem not answered by the return map alone. The exact clock separates the ordinary critical scale from the stronger midpoint slowdown and explains why a continuous initial ensemble sees only the ordinary scale. This is a natural all-parameter transient result for a known map, not a new classification of its cycles or a full-plane theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
