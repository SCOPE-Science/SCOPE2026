# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. For sides \((b-d,b,b+d)\), Heron's formula gives the exact reduction to \(b=2x\) and \(x^2-d^2=3y^2\), with area \(K=3xy\). Removing the common side gcd yields coprime \(X,Y,D\) with \(X^2-D^2=3Y^2\), \(D\) odd, and \(X,Y\) of opposite parity. Since every Heronian area here is divisible by \(6\), two-prime support forces support exactly \(\{2,3\}\). Then \(3\nmid X\), so \(X=2^A\), while coprimality forces \(Y=3^B\). If \(B\ge1\), the square equation is impossible modulo \(8\) for \(A\ge2\), and negative for \(A=1\). Hence \(B=0\), and \((2^A-D)(2^A+D)=3\) gives \(A=1,D=1\), namely the primitive \(3,4,5\) triangle. Scaling preserves exactly two area primes precisely for \(t=2^u3^v\). The bounded scan is supporting evidence only.

Originality: PASS. MacDougall's arithmetic-progression parameterization and Read's complete 2025 HAP treatment were both inspected in full. Read gives a complete primitive parameterization and the exact area formula, and also proves that \(3,4,5\) is the only primitive right triangle in the class, but neither source states or implies without an additional Diophantine argument that exactly two distinct area primes force the \(3,4,5\) similarity class. Published-record and targeted searches found no earlier exact prime-support classification.

Scientific value: PASS. Minimal prime support of the integer area is a natural arithmetic invariant of a classical Diophantine family. The theorem gives a complete infinite classification, identifies a unique primitive shape, and converts a broad HAP parameterization into a sharp smoothness statement rather than reporting a bounded census.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
