# Independent mathematical audit

## correctness

PASS

Substituting f=-λy in the printed rule and dividing by the positive implicit multiplier gives A=(16-9s)/(48+25s), B=(32-30s)/(48+25s) on y_n and y_{n+1}, respectively. With A>0 and B>=0 through s_0=16/15, induction gives strict positivity, including B=0. At s>=16/9 one has A<=0, B<0, so y_2=A+B exp(-s)<0 even at the endpoint. Between these values the characteristic roots are distinct, with r_-<0<r_+<|r_-|. For q=(2-s)/(2+s)>0, the numerator of q^2-Bq-A over (s+2)^2(48+25s) is exactly 4s^3. Thus q>r_+, and exp(-s)>q by 2 artanh(s/2)>s. This proves c_+>0>c_- and excludes the exceptional pure-positive-root start. Odd iterates are positive, and y_{2j}<0 exactly when 2j log(|r_-|/r_+) exceeds log(c_+/(-c_-)). Taking floor plus one is valid even if an earlier iterate is exactly zero. At s_0, A=3/35, B'=−45/112; the log-root ratio equals log((sqrt(B^2+4A)-B)/(sqrt(B^2+4A)+B)), with first-order term 45(s-s_0)/(112 sqrt(3/35)). The startup coefficient ratio tends to the stated finite positive ratio, and the floor changes the index by at most two. This yields the stated inverse-distance constant, independently evaluated as 1.8343063999443295… .

## originality

PASS

The method, root-stability properties and a sufficient arbitrary-positive-history threshold are not new. The same-family phase diagram also gives both transition values and identifies the single exceptional positive ratio between them. The distinct contribution is the exact exponential starter's strict nonresonance throughout that open interval and the resulting parity, strict first-negative index and sharp delay coefficient. The broader diagram does not evaluate those features; its later catalog date is not needed to separate the statements.

## value

PASS

The exact scalar sign test is meaningful for a named stiff integrator: A-stability does not protect a positive decaying scalar mode. The sharp index estimates show why an above-threshold step may pass any fixed finite positivity test, and when negativity first appears under exact startup. This gives a usable diagnostic beyond the already-known coefficientwise guarantee and does not claim analogous behavior for arbitrary starts or nonlinear systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
