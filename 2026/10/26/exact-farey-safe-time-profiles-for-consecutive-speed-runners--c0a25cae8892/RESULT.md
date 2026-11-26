# Exact Farey safe-time profiles for consecutive-speed runners

## Finding

For each integer \(n\ge2\), let \(\|x\|=\min_{j\in\mathbb Z}|x-j|\) and define the simultaneous safe-time profile
\[
G_n(\delta)=\operatorname{Leb}\{t\in\mathbb R/\mathbb Z:\|kt\|>\delta\text{ for all }1\le k\le n\},\qquad \delta\ge0.
\]
Then
\[
G_n(\delta)=\sum_{\substack{1\le q,r\le n\\ (q,r)=1,\;q+r>n}}\frac{(1-\delta(q+r))_+}{qr},\qquad x_+=\max(x,0),
\]
where the pair \((q,r)\) is ordered. The positive-threshold slope jumps are exactly at \(\delta=1/s\) for \(n+1\le s\le 2n-1\), omitting \(s=2n-2\) when \(n\) is even. In particular the strict safe-time set is empty for \(\delta\ge 1/(n+1)\).

At the union-bound radius,
\[
G_n(1/(2n))=1-\frac1n\sum_{q=1}^n\frac{\varphi(q)}q\longrightarrow 1-\frac6{\pi^2}.
\]
For \(1/(n+2)\le\delta\le1/(n+1)\) the last segment is
\[
G_n(\delta)=\frac{2(1-(n+1)\delta)}{n+1}\sum_{\substack{1\le j\le n\\(j,n+1)=1}}\frac1j.
\]
For \(1/(n+2)<\delta<1/(n+1)\) the strict safe-time set has exactly \(\varphi(n+1)\) open connected components. At \(\delta=1/(n+1)\), the non-strict inequalities \(\|kt\|\ge\delta\) hold exactly at the reduced fractions of denominator \(n+1\), not on open intervals.

## Assumptions and scope

The speeds are exactly \(1,\ldots,n\), the threshold is common to them all, and the measure is normalized on the circle. There is no assertion about unequal thresholds, other speed sets, or optimality among speed sets of cardinality \(n\).

## Proof

Take successive fractions \(a/q<b/r\) in the Farey sequence of order \(n\) on \([0,1]\), using \(0/1\) and \(1/1\) as separate endpoints of the list but identifying them on the circle. The classical adjacency criterion gives \(bq-ar=1\) and \(q+r>n\). Conversely, for a coprime ordered pair of allowed denominators with \(q+r>n\), choose the unique \(0\le a<q\) with \(ar\equiv-1\pmod q\) and set \(b=(1+ar)/q\). Here \(1\le b\le r\). The determinant identity gives reduced fractions at distance \(1/(qr)\), and the sum condition makes them Farey neighbors. This also handles the pair at each endpoint of the list.

We show directly that on this Farey gap the pointwise minimum of the distances is
\[
\min_{1\le k\le n}\|kt\|=\min(qt-a,b-rt), \qquad a/q\le t\le b/r.
\]
Write \(X=qt-a\ge0\), \(Y=b-rt\ge0\). The two vectors \((a,q),(b,r)\) form an integral basis of \(\mathbb Z^2\) because their determinant has modulus one. For every \(p\in\mathbb Z\) and \(1\le k\le n\), write \((p,k)=u(a,q)+v(b,r)\) with integers \(u,v\). They cannot both be positive, since this would give \(k\ge q+r>n\); they cannot both be nonpositive, since \(k>0\). If \(u\ge1,v\le0\) then \(kt-p=uX-vY\ge X\); if \(v\ge1,u\le0\) then \(p-kt=vY-uX\ge Y\). This gives the lower bound for every \(|kt-p|\). The two Farey endpoints supply the candidates \((p,k)=(a,q),(b,r)\), proving equality.

Therefore the strict conditions in the gap select the open interval from \((a+\delta)/q\) to \((b-\delta)/r\) if those endpoints are in increasing order, and otherwise select nothing. The length is \((1-\delta(q+r))_+/(qr)\). These intervals lie in disjoint Farey gaps and the original Farey centers are not safe. Summing yields the profile for every \(\delta\ge0\). Since \(q+r\ge n+1\), none of the intervals survives at or above \(1/(n+1)\).

Each summand has a positive slope jump \((q+r)/(qr)\) at \(1/(q+r)\), so jumps do not cancel. The attainable sums have \(n+1\le s\le2n-1\), as \(q=r=n\) is not coprime. Every odd \(s\) in range is attained by \(((s-1)/2,(s+1)/2)\). If \(s=2m\) with \(m\) even, \((m-1,m+1)\) is coprime and in range. If \(m\) is odd and \(s\le 2n-4\), use \((m-2,m+2)\) (here \(m\ge3\)): the entries are odd and a common divisor must divide four. The only remaining case is \(m=n-1\) odd, that is, \(n\) even and \(s=2n-2\) in range. The only possibilities up to order are \((n-2,n)\) and \((n-1,n-1)\), neither coprime. This gives the stated parity exception, including \(n=2\), for which the omitted index is outside the range.

At \(\delta=1/(2n)\) no term is clipped. The zeroth-order sum \(\sum 1/(qr)\) is the total length of all Farey gaps, namely one. In the slope sum each Farey center of denominator \(q\) contributes \(1/q\) to each of its two incident gaps; there are \(\varphi(q)\) such centers with \(\varphi(1)=1\). The claimed identity follows. The asymptotic \(\sum_{q\le n}\varphi(q)/q=(6/\pi^2)n+O(\log n)\) follows by inserting \(\varphi(q)/q=\sum_{d\mid q}\mu(d)/d\), where \(\mu\) is the Möbius function, and summing the floors \(\lfloor n/d\rfloor\).

In the final segment only sums \(q+r=n+1\) contribute nonzero terms; at its lower endpoint the terms with \(q+r=n+2\) are already zero. The first denominators of the surviving pairs range over the reduced residues \(j\) modulo \(n+1\). The identity
\[
\frac1{j(n+1-j)}=\frac{1}{n+1}\left(\frac1j+\frac1{n+1-j}\right)
\]
gives the harmonic sum. In the open segment, each such pair supplies one nonempty interval and distinct pairs occupy separate components. At the critical endpoint these pairs have touching endpoints at their mediants \((a+b)/(q+r)\); no other pair admits a point satisfying both non-strict inequalities. These mediants are reduced since \(bq-ar=1\), and are distinct because they are in disjoint gaps. There are \(\varphi(n+1)\) of them, exhausting the reduced fractions of that denominator.

## Verification

The accompanying `verify.py` uses standard-library exact rational arithmetic to check 480 thresholds for \(2\le n\le21\) against direct unions of the forbidden arcs for the unreduced speeds. It also checks the attainable denominator sums and the totient and final-segment identities in that range. The expected last line is `CERTIFICATE_OK sizes=20 exact_profile_points=480 kink_classifications=20`. The proof above treats the infinite domain; the finite tests provide corroboration only.

## Relationship to prior work and limitations

The Farey adjacency theorem and the scalar critical radius for consecutive speeds are classical inputs or consequences; novelty is not claimed for them or for the underlying pointwise Farey geometry. The distributional calculation identifies the entire finite-threshold law together with its precise kink spectrum, parity exception, and benchmark mass. Hu and Jing study the uncovered-time measure for arbitrary speed sets at the benchmark threshold and give a uniform positive lower bound, not the exact consecutive-speed profile. Jensen gives two-speed results with mixed thresholds. Zhang studies the uncovered region at one threshold after deleting a speed, not the intact all-threshold profile. The exact formula is elementary and equivalent formulations may exist in Farey or Diophantine approximation literature. Neither a general Lonely Runner bound nor exhaustive historical priority is asserted.

## References

1. Xiyu Hu and Yifan Jing, *Near optimal gap in the Lonely Runner Conjecture*, https://arxiv.org/abs/2610.23790.
2. Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, https://arxiv.org/abs/2605.27941.
3. Yuhan Zhang, *Single-speed modifications of the tight Lonely Runner instance: an effective bound and the complete classification for r = 2*, https://arxiv.org/abs/2608.13599.
