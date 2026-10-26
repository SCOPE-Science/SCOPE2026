# Exact 2-adic convergence rate for a quadratic map with an attracting 2-cycle

## Finding

Let \(\lambda\in\mathbb Z_2\) satisfy \(\lambda\equiv3\pmod4\), and define
\[
f_\lambda(x)=x^2-\lambda\qquad (x\in\mathbb Z_2).
\]
There is a unique 2-cycle \(\alpha\leftrightarrow\beta\), with
\(\alpha\equiv1\pmod4\) and \(\beta\equiv2\pmod4\), and every orbit converges alternately to its two points.

The convergence has an exact valuation law. Put \(B=\beta+8\mathbb Z_2\). For
\(y=\beta+u\in B\) with \(k=v_2(u)\ge3\), including \(k=+\infty\) when \(u=0\), one has
\[
v_2(f_\lambda^{2j}(y)-\beta)=k+3j,\qquad
v_2(f_\lambda^{2j+1}(y)-\alpha)=k+2+3j
\]
for every integer \(j\ge0\).

This yields an exact pointwise transient formula on every finite quotient. For \(N\ge1\) and \(y\in B\), define
\[
k_N(y)=\min\{N,v_2(y-\beta)\},\quad d_N(y)=N-k_N(y),
\]
and
\[
h_N(y)=
\begin{cases}
0,&d_N(y)=0,\\
2\lfloor d_N(y)/3\rfloor,&d_N(y)>0\text{ and }3\mid d_N(y),\\
2\lfloor d_N(y)/3\rfloor+1,&d_N(y)>0\text{ and }3\nmid d_N(y).
\end{cases}
\]
Then \(h_N(y)\) is the least additional time for \(y\bmod2^N\) to enter the cycle modulo \(2^N\).

For any residue \(x\bmod2^N\), let \(T_N(x)\) be its least time to enter the cycle
\(\{\alpha,\beta\}\bmod2^N\). The exact formula is
\[
T_N(x)=
\begin{cases}
0,&x\equiv\alpha\text{ or }\beta\pmod{2^N},\\
1+h_N(f_\lambda(x)),&x\text{ odd and not already on the cycle},\\
1,&x\text{ even and }f_\lambda(x)\equiv\alpha\pmod{2^N},\\
2+h_N(f_\lambda^2(x)),&\text{otherwise}.
\end{cases}
\]
The odd branch enters \(B\) after one iterate; the remaining even branch enters \(B\) after two. The exceptional cases handle residues already on the cycle or mapping to it one step earlier. Thus the formula gives the globally minimal preperiod of each residue, not merely an upper bound.

## Assumptions and scope

The domain is the ring \(\mathbb Z_2\) of 2-adic integers. The parameter condition
\(\lambda\equiv3\pmod4\) is essential. The valuation is normalized by
\(v_2(2)=1\) and \(v_2(0)=+\infty\); congruence modulo \(2^N\) is equivalent to valuation at least \(N\). The ball \(B\) is the residue class
\((1-\lambda)+8\mathbb Z_2\). The finite-quotient formula uses the cycle residues induced by the unique 2-adic cycle. No claim is made for parameters outside this congruence class.

## Proof

Write \(g=f_\lambda^2\) and \(B=(1-\lambda)+8\mathbb Z_2\). Since
\(\lambda\equiv3\pmod4\), its residue modulo \(8\) is \(3\) or \(7\). Every \(x\in B\) is therefore congruent to \(6\) or \(2\) modulo \(8\), so \(v_2(x)=1\). It follows that
\(f_\lambda(x)\equiv4-\lambda\pmod8\) and
\(g(x)\equiv1-\lambda\pmod8\), hence \(g(B)\subseteq B\).

For \(x,y\in B\),
\[
g(x)-g(y)=(x-y)(x+y)(x^2+y^2-2\lambda).
\]
The first two points are both \(2\pmod4\), so \(4\mid x+y\). Also
\(x^2+y^2\equiv0\pmod4\) while \(2\lambda\equiv2\pmod4\), so
\(v_2(x^2+y^2-2\lambda)=1\). Therefore
\[
v_2(g(x)-g(y))\ge v_2(x-y)+3.
\]
Thus \(g\) is a strict contraction of the complete metric space \(B\), and has a unique fixed point \(\beta\in B\). Set \(\alpha=f_\lambda(\beta)\). Then \(f_\lambda(\alpha)=\beta\), \(\beta\) is even, and \(\alpha\) is odd; the congruences above give
\(\beta\equiv2\pmod4\) and \(\alpha\equiv1\pmod4\). This is a 2-cycle.

Every odd \(x\) satisfies \(f_\lambda(x)\equiv1-\lambda\pmod8\), so its first image lies in \(B\). Every even \(x\) has odd first image, and its second image is congruent to \(1-\lambda\pmod8\), so it enters \(B\) by time two. Since \(g\) is a contraction on \(B\), every even subsequence after entry converges to \(\beta\), and the intervening odd subsequence converges to \(\alpha\). A periodic orbit in a finite set cannot have a convergent subsequence unless that subsequence is eventually constant; consequently no other periodic orbit exists.

For the exact rate, write \(y=\beta+u\), where \(k=v_2(u)\ge3\). First,
\[
f_\lambda(y)-\alpha=u(2\beta+u).
\]
Because \(v_2(2\beta)=2<k\), the factor \(2\beta+u\) has valuation exactly \(2\), giving
\(v_2(f_\lambda(y)-\alpha)=k+2\).

Expanding the second iterate at \(\beta\) gives
\[
g(\beta+u)-\beta
=u\bigl(4\alpha\beta+(6\beta^2-2\lambda)u+4\beta u^2+u^3\bigr).
\]
Since \(\alpha\) is odd and \(v_2(\beta)=1\),
\(v_2(4\alpha\beta)=3\). Moreover,
\(6\beta^2-2\lambda=2(3\beta^2-\lambda)\) has valuation \(1\), because
\(4\mid\beta^2\) and \(\lambda\) is odd. The remaining terms inside the parentheses have valuations at least \(k+1\), \(3+2k\), and \(3k\), respectively, all strictly greater than \(3\). Hence
\[
v_2(g(y)-\beta)=k+3.
\]
Applying these two identities inductively proves both valuation formulas for every \(j\ge0\).

The definition of \(h_N\) follows by comparing the even-time error exponent \(k+3j\) and odd-time exponent \(k+2+3j\). For \(x\) odd, \(f_\lambda(x)\in B\), and \(x\) itself cannot be congruent to \(\beta\) because their parities differ; the only time-zero exception is \(x\equiv\alpha\). For even \(x\), \(x\) itself can be on the cycle only at \(\beta\); if its first image is congruent to \(\alpha\), its least entry time is one. In every other even case, neither time zero nor time one is on the cycle, and \(f_\lambda^2(x)\in B\), so the least entry time is exactly two plus the tail time \(h_N\). This proves the global formula for every \(N\ge1\).

## Verification

The contraction identity, the expansion of \(g(\beta+u)\), and the valuations of every term are displayed in the proof. The leading term in the second-iterate expansion has valuation \(3\), while all competing terms have strictly larger valuation for \(k\ge3\); there is no cancellation at the leading valuation. The finite-quotient formula explicitly separates time-zero, time-one, and basin-entry cases. No finite experiment is used as an infinite proof.

## Relationship to prior work

Fan and Liao's treatment of quadratic \(2\)-adic polynomials states that for
\(f_\lambda(x)=x^2-\lambda\) with \(\lambda\equiv3\pmod4\), the whole space
\(\mathbb Z_2\) is attracted to a 2-cycle with one point in \(1+4\mathbb Z_2\) and the other in \(2+4\mathbb Z_2\). The theorem and its proof establish the qualitative basin and cycle structure. The exact three-unit valuation gain per two iterates and the pointwise minimal-preperiod formula on every finite quotient above are a quantitative refinement; the qualitative classification itself is not claimed as new.

## Limitations

The result gives the minimal preperiod of each individual residue but does not aggregate those values into a histogram counting residues at each depth. The proof does not address \(\lambda\not\equiv3\pmod4\). The literature comparison is bounded to the directly relevant primary source and targeted searches; absence of an exact wording match is not proof that no related quantitative statement exists.

## References

- A.-H. Fan and L. Liao, “On minimal decomposition of \(p\)-adic polynomial dynamical systems,” *Advances in Mathematics* 228 (2011), 2116–2144. First public version: 2010-10-27. [arXiv:1010.5583](https://arxiv.org/abs/1010.5583); DOI: [10.1016/j.aim.2011.06.032](https://doi.org/10.1016/j.aim.2011.06.032).
