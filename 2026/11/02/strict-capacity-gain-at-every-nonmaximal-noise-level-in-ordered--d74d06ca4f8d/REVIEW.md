# Independent mathematical audit

## correctness

PASS

The three rows have equal conditional entropy, so capacity maximizes output entropy. For t=1−2p>0 the two-bit transition matrix is invertible, so distinct input laws give distinct outputs; strict concavity and reverse-complement symmetry give the unique symmetric optimizer. The two endpoint slopes of the symmetric output entropy are t² ln((1+t²)/(1−t²))>0 and t ln((1−t)/(1+t))<0 for 0<t<1, proving full support and strict gain over the equiprobable restriction. At p=0 the respective alphabets have three and two distinguishable letters; at p=1/2 all rows coincide. Independently group outputs by whether their bits agree: put x=t², q=(1−x)/2+xβ, z=tβ/q. Output entropy in nats is ln 2+h(q)−q[(1+z)ln(1+z)+(1−z)ln(1−z)]/2. The analytic stationarity equation divided by t² has value −2β at t=0 and nonzero β derivative. Parity and the implicit-function theorem make B=β/x analytic near x=0. The grouped gain divided by x³ expands as 2B−B²−3xB²+x²(2B/3−B²+2B³)+O(x³). Stationarity gives B=1−3x+(34/3)x²+O(x³); substitution gives the gain coefficients 1, −3, 32/3 in nats, with the asserted bits conversion. The independent finite numerical checks corroborate these coefficients, not the all-noise result.

## originality

PASS

The exact channel, symmetry reduction, and repetition baseline are known. The strongest exact-model prior gives a numerical comparison, not the strict all-noise conclusion and sharp high-noise expansion. Credit is limited to the strict/interior-optimizer analysis and the quantified cancellation, not the model or the optimization itself.

## value

PASS

For the exact fixed channel in which prior numerical curves were nearly indistinguishable, the result resolves whether there is a genuine advantage and shows why it is hard to see: the optimizing mixed-symbol weight is second order in t, and the advantage is sixth order. The explicit higher terms make this a quantitative explanation of a prior comparison, not just a positive but arbitrarily tiny numerical improvement or a claim about practical storage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
